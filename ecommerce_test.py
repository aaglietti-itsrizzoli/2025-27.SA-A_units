from datetime import date
import pytest

from ecommerce import (
    calcola_prezzo_scontato,
    applica_codice_sconto,
    calcola_iva,
    crea_riga_carrello,
    calcola_totale_carrello,
    svuota_articoli_esauriti,
    calcola_totale_ordine,
    calcola_costo_spedizione,
    stima_data_consegna,
    calcola_punti_fedelta,
    promuovi_livello_cliente,
    riepilogo_cliente,
)


# ---------------------------------------------------------------------------
# Catalogo e prezzi
# ---------------------------------------------------------------------------

def test_calcola_prezzo_scontato_valido():
    assert calcola_prezzo_scontato(100.0, 20) == 80.0
    assert calcola_prezzo_scontato(49.99, 10) == 44.99


def test_calcola_prezzo_scontato_prezzo_negativo_eccezione():
    with pytest.raises(ValueError, match="il prezzo non può essere negativo"):
        calcola_prezzo_scontato(-10.0, 20)


def test_calcola_prezzo_scontato_percentuale_non_valida_eccezione():
    with pytest.raises(ValueError, match="la percentuale di sconto deve essere tra 0 e 100"):
        calcola_prezzo_scontato(100.0, -5)

    with pytest.raises(ValueError, match="la percentuale di sconto deve essere tra 0 e 100"):
        calcola_prezzo_scontato(100.0, 105)


def test_applica_codice_sconto_esistente():
    tabella = {"SUMMER20": 20, "BLACKFRIDAY": 50}
    assert applica_codice_sconto(100.0, "SUMMER20", tabella) == 80.0


def test_applica_codice_sconto_inesistente():
    tabella = {"SUMMER20": 20}
    assert applica_codice_sconto(100.0, "NONESISTE", tabella) == 100.0


def test_calcola_iva_default_e_personalizzata():
    assert calcola_iva(100.0) == 122.0
    assert calcola_iva(100.0, aliquota=10) == 110.0


def test_calcola_iva_valori_negativi_eccezione():
    with pytest.raises(ValueError, match="il prezzo netto non può essere negativo"):
        calcola_iva(-50.0, 22)

    with pytest.raises(ValueError, match="l'aliquota non può essere negativa"):
        calcola_iva(100.0, -10)


# ---------------------------------------------------------------------------
# Carrello
# ---------------------------------------------------------------------------

def test_crea_riga_carrello_valida():
    riga = crea_riga_carrello("Laptop", 500.0, 2)
    assert riga == {
        "nome": "Laptop",
        "prezzo_unitario": 500.0,
        "quantita": 2,
        "subtotale": 1000.0,
    }


def test_crea_riga_carrello_quantita_o_prezzo_non_validi_eccezione():
    with pytest.raises(ValueError, match="la quantità deve essere maggiore di zero"):
        crea_riga_carrello("Mouse", 20.0, 0)

    with pytest.raises(ValueError, match="la quantità deve essere maggiore di zero"):
        crea_riga_carrello("Mouse", 20.0, -1)

    with pytest.raises(ValueError, match="il prezzo unitario non può essere negativo"):
        crea_riga_carrello("Mouse", -10.0, 1)


def test_calcola_totale_carrello_vuoto_e_con_elementi():
    assert calcola_totale_carrello([]) == 0.0

    righe = [
        {"subtotale": 10.50},
        {"subtotale": 20.25},
    ]
    assert calcola_totale_carrello(righe) == 30.75


def test_svuota_articoli_esauriti():
    carrello = [
        {"nome": "Tastiera", "subtotale": 30.0},
        {"nome": "Mouse", "subtotale": 15.0},
        {"nome": "Cuffie", "subtotale": 50.0},
    ]
    magazzino = {
        "Tastiera": 5,
        "Mouse": 0,
        # Cuffie assenti
    }
    risultato = svuota_articoli_esauriti(carrello, magazzino)
    assert len(risultato) == 1
    assert risultato[0]["nome"] == "Tastiera"


def test_calcola_totale_ordine_completo():
    carrello = [
        {"nome": "Libro", "subtotale": 20.0},
        {"nome": "Penna", "subtotale": 5.0},
    ]
    magazzino = {"Libro": 10, "Penna": 0}
    tabella_sconti = {"WELCOME10": 10}

    ordine = calcola_totale_ordine(
        righe_carrello=carrello,
        magazzino=magazzino,
        codice_sconto="WELCOME10",
        tabella_codici=tabella_sconti,
        aliquota_iva=22,
    )

    assert len(ordine["righe_valide"]) == 1
    assert ordine["totale_netto"] == 18.0  # 20 - 10%
    assert ordine["totale_lordo"] == 21.96  # 18 * 1.22


# ---------------------------------------------------------------------------
# Spedizione
# ---------------------------------------------------------------------------

def test_calcola_costo_spedizione_standard_ed_espressa():
    # costo = 3.0 + 0.5 * 10 + 0.02 * 100 = 3.0 + 5.0 + 2.0 = 10.0
    assert calcola_costo_spedizione(peso_kg=10, distanza_km=100, espressa=False) == 10.0
    assert calcola_costo_spedizione(peso_kg=10, distanza_km=100, espressa=True) == 20.0


def test_calcola_costo_spedizione_limiti_e_valori_negativi_eccezione():
    with pytest.raises(ValueError, match="peso e distanza non possono essere negativi"):
        calcola_costo_spedizione(-1, 100)

    with pytest.raises(ValueError, match="peso e distanza non possono essere negativi"):
        calcola_costo_spedizione(10, -50)

    with pytest.raises(ValueError, match="peso massimo consentito: 30 kg"):
        calcola_costo_spedizione(30.1, 100)


def test_stima_data_consegna_saltando_weekend():
    # Venerdì 2 Ottobre 2026
    venerdi = date(2026, 10, 2)
    # 2 giorni lavorativi -> Sabato (salto), Domenica (salto), Lunedì (1), Martedì (2) -> 6 Ottobre
    consegna = stima_data_consegna(venerdi, 2)
    assert consegna == date(2026, 10, 6)


def test_stima_data_consegna_giorni_negativi_eccezione():
    with pytest.raises(ValueError, match="i giorni lavorativi non possono essere negativi"):
        stima_data_consegna(date(2026, 10, 2), -1)


# ---------------------------------------------------------------------------
# Fedeltà cliente / punti
# ---------------------------------------------------------------------------

def test_calcola_punti_fedelta_zero_punti_per_dieci_euro_acquisto():
    assert calcola_punti_fedelta(3) == 0


def test_calcola_punti_fedelta_con_moltiplicatore():
    assert calcola_punti_fedelta(25, moltiplicatore=2) == 4


def test_calcola_punti_fedelta_valori_non_validi_eccezione():
    with pytest.raises(ValueError, match="il totale speso non può essere negativo"):
        calcola_punti_fedelta(-10)

    with pytest.raises(ValueError, match="il moltiplicatore deve essere positivo"):
        calcola_punti_fedelta(50, moltiplicatore=0)


def test_promuovi_livello_cliente_scaglioni():
    assert promuovi_livello_cliente(0) == "bronze"
    assert promuovi_livello_cliente(99) == "bronze"
    assert promuovi_livello_cliente(100) == "silver"
    assert promuovi_livello_cliente(499) == "silver"
    assert promuovi_livello_cliente(500) == "gold"
    assert promuovi_livello_cliente(1999) == "gold"
    assert promuovi_livello_cliente(2000) == "platinum"


def test_promuovi_livello_cliente_punti_negativi_eccezione():
    with pytest.raises(ValueError, match="i punti totali non possono essere negativi"):
        promuovi_livello_cliente(-1)


def test_riepilogo_cliente_completo():
    riepilogo = riepilogo_cliente(totale_speso_storico=120, moltiplicatore=1)
    assert riepilogo == {
        "totale_speso": 120,
        "punti": 12,
        "livello": "silver",
    }