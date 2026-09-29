from datetime import date
import pytest

from ecommerce import (
    applica_codice_sconto,
    calcola_costo_spedizione,
    calcola_iva,
    calcola_prezzo_scontato,
    calcola_punti_fedelta,
    calcola_totale_carrello,
    calcola_totale_ordine,
    crea_riga_carrello,
    promuovi_livello_cliente,
    riepilogo_cliente,
    stima_data_consegna,
    svuota_articoli_esauriti,
)


# ---------------------------------------------------------------------------
# Test Catalogo e Prezzi
# ---------------------------------------------------------------------------

def test_calcola_prezzo_scontato_valido():
    assert calcola_prezzo_scontato(100.0, 20) == 80.0
    assert calcola_prezzo_scontato(50.0, 0) == 50.0
    assert calcola_prezzo_scontato(50.0, 100) == 0.0


def test_calcola_prezzo_scontato_arrotondamento():
    # 10.55 sconto 15% = 8.9675 -> 8.97
    assert calcola_prezzo_scontato(10.55, 15) == 8.97


def test_calcola_prezzo_scontato_eccezioni():
    with pytest.raises(ValueError, match="non può essere negativo"):
        calcola_prezzo_scontato(-10, 20)

    with pytest.raises(ValueError, match="tra 0 e 100"):
        calcola_prezzo_scontato(100, -5)

    with pytest.raises(ValueError, match="tra 0 e 100"):
        calcola_prezzo_scontato(100, 105)


def test_applica_codice_sconto_esistente():
    tabella = {"ESTATE10": 10, "VIP30": 30}
    assert applica_codice_sconto(100, "ESTATE10", tabella) == 90.0


def test_applica_codice_sconto_inesistente():
    tabella = {"ESTATE10": 10}
    assert applica_codice_sconto(100, "CODICE_INVALUTO", tabella) == 100.0


def test_calcola_iva_default_e_custom():
    assert calcola_iva(100) == 122.0
    assert calcola_iva(100, aliquota=10) == 110.0


def test_calcola_iva_eccezioni():
    with pytest.raises(ValueError, match="prezzo netto non può essere negativo"):
        calcola_iva(-50)

    with pytest.raises(ValueError, match="aliquota non può essere negativa"):
        calcola_iva(100, aliquota=-10)


# ---------------------------------------------------------------------------
# Test Carrello
# ---------------------------------------------------------------------------

def test_crea_riga_carrello_valida():
    riga = crea_riga_carrello("T-Shirt", 19.99, 2)
    assert riga == {
        "nome": "T-Shirt",
        "prezzo_unitario": 19.99,
        "quantita": 2,
        "subtotale": 39.98,
    }


def test_crea_riga_carrello_eccezioni():
    with pytest.raises(ValueError, match="quantità deve essere maggiore di zero"):
        crea_riga_carrello("T-Shirt", 10.0, 0)

    with pytest.raises(ValueError, match="prezzo unitario non può essere negativo"):
        crea_riga_carrello("T-Shirt", -5.0, 1)


def test_calcola_totale_carrello():
    carrello = [
        {"subtotale": 10.50},
        {"subtotale": 20.25},
    ]
    assert calcola_totale_carrello(carrello) == 30.75


def test_calcola_totale_carrello_vuoto():
    assert calcola_totale_carrello([]) == 0.0


def test_svuota_articoli_esauriti():
    carrello = [
        {"nome": "Mouse"},
        {"nome": "Tastiera"},
        {"nome": "Monitor"},
    ]
    magazzino = {"Mouse": 5, "Tastiera": 0}  # Monitor non è in magazzino

    risultato = svuota_articoli_esauriti(carrello, magazzino)
    
    # Mantiene solo 'Mouse'
    assert risultato == [{"nome": "Mouse"}]
    # Verifica immutabilità della lista originale
    assert len(carrello) == 3


def test_calcola_totale_ordine():
    carrello = [
        {"nome": "Libro", "subtotale": 20.0},
        {"nome": "Penna", "subtotale": 5.0},
    ]
    magazzino = {"Libro": 10, "Penna": 0}
    codici = {"PROMO10": 10}

    # Solo 'Libro' (20.0), sconto 10% -> netto 18.0, IVA 22% -> lordo 21.96
    ordine = calcola_totale_ordine(
        righe_carrello=carrello,
        magazzino=magazzino,
        codice_sconto="PROMO10",
        tabella_codici=codici,
        aliquota_iva=22,
    )

    assert len(ordine["righe_valide"]) == 1
    assert ordine["totale_netto"] == 18.0
    assert ordine["totale_lordo"] == 21.96


# ---------------------------------------------------------------------------
# Test Spedizione
# ---------------------------------------------------------------------------

def test_calcola_costo_spedizione_standard_e_espressa():
    # 3.0 + (0.5 * 2) + (0.02 * 100) = 3 + 1 + 2 = 6.0
    assert calcola_costo_spedizione(peso_kg=2, distanza_km=100, espressa=False) == 6.0
    # Espressa -> 6.0 * 2 = 12.0
    assert calcola_costo_spedizione(peso_kg=2, distanza_km=100, espressa=True) == 12.0


def test_calcola_costo_spedizione_eccezioni():
    with pytest.raises(ValueError, match="non possono essere negativi"):
        calcola_costo_spedizione(-1, 100)

    with pytest.raises(ValueError, match="peso massimo consentito"):
        calcola_costo_spedizione(31, 50)


def test_stima_data_consegna_senza_weekend():
    # Lunedì 5 Ottobre 2026 + 3 giorni lavorativi -> Giovedì 8 Ottobre 2026
    lunedì = date(2026, 10, 5)
    assert stima_data_consegna(lunedì, 3) == date(2026, 10, 8)


def test_stima_data_consegna_con_weekend():
    # Venerdì 9 Ottobre 2026 + 2 giorni lavorativi -> Martedì 13 Ottobre 2026
    venerdì = date(2026, 10, 9)
    assert stima_data_consegna(venerdì, 2) == date(2026, 10, 13)


def test_stima_data_consegna_eccezione():
    with pytest.raises(ValueError, match="non possono essere negativi"):
        stima_data_consegna(date(2026, 10, 5), -1)


# ---------------------------------------------------------------------------
# Test Fedeltà cliente / Punti
# ---------------------------------------------------------------------------

# Scenario da ecommerce.gherkin.txt
def test_calcola_punti_fedelta_zero_punti_per_dieci_euro_acquisto():
    # Given un acquisto di 3 euro
    totale_speso = 3
    # When un cliente conclude un acquisto fn:calcola_punti_fedelta
    punti = calcola_punti_fedelta(totale_speso)
    # Then il cliente riceve 0 punti fedeltà
    assert punti == 0


def test_calcola_punti_fedelta_con_moltiplicatore():
    # 25 euro -> 2 punti base * moltiplicatore 3 = 6 punti
    assert calcola_punti_fedelta(25, moltiplicatore=3) == 6


def test_calcola_punti_fedelta_eccezioni():
    with pytest.raises(ValueError, match="non può essere negativo"):
        calcola_punti_fedelta(-10)

    with pytest.raises(ValueError, match="deve essere positivo"):
        calcola_punti_fedelta(100, moltiplicatore=0)


def test_promuovi_livello_cliente():
    assert promuovi_livello_cliente(50) == "bronze"
    assert promuovi_livello_cliente(100) == "silver"
    assert promuovi_livello_cliente(500) == "gold"
    assert promuovi_livello_cliente(2000) == "platinum"


def test_promuovi_livello_cliente_eccezione():
    with pytest.raises(ValueError, match="non possono essere negativi"):
        promuovi_livello_cliente(-1)


def test_riepilogo_cliente():
    riepilogo = riepilogo_cliente(totale_speso_storico=1500, moltiplicatore=1)
    assert riepilogo == {
        "totale_speso": 1500,
        "punti": 150,
        "livello": "silver",
    }