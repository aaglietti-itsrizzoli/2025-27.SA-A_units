from datetime import date
import pytest
import ecommerce


# ---------------------------------------------------------------------------
# Test Catalogo e Prezzi
# ---------------------------------------------------------------------------

def test_calcola_prezzo_scontato_valido():
    assert ecommerce.calcola_prezzo_scontato(100.0, 20) == 80.0
    assert ecommerce.calcola_prezzo_scontato(0, 50) == 0.0


def test_calcola_prezzo_scontato_errori():
    with pytest.raises(ValueError, match="il prezzo non può essere negativo"):
        ecommerce.calcola_prezzo_scontato(-10.0, 20)

    with pytest.raises(ValueError, match="la percentuale di sconto deve essere tra 0 e 100"):
        ecommerce.calcola_prezzo_scontato(100.0, -5)

    with pytest.raises(ValueError, match="la percentuale di sconto deve essere tra 0 e 100"):
        ecommerce.calcola_prezzo_scontato(100.0, 105)


def test_applica_codice_sconto():
    tabella = {"SUMMER10": 10, "WELCOME20": 20}
    assert ecommerce.applica_codice_sconto(100.0, "SUMMER10", tabella) == 90.0
    assert ecommerce.applica_codice_sconto(100.0, "CODICE_ERRATO", tabella) == 100.0


def test_calcola_iva():
    assert ecommerce.calcola_iva(100.0) == 122.0
    assert ecommerce.calcola_iva(100.0, aliquota=10) == 110.0


def test_calcola_iva_errori():
    with pytest.raises(ValueError, match="il prezzo netto non può essere negativo"):
        ecommerce.calcola_iva(-50.0)

    with pytest.raises(ValueError, match="l'aliquota non può essere negativa"):
        ecommerce.calcola_iva(100.0, aliquota=-10)


# ---------------------------------------------------------------------------
# Test Carrello e Ordini
# ---------------------------------------------------------------------------

def test_crea_riga_carrello_valida():
    riga = ecommerce.crea_riga_carrello("Tastiera", 50.0, 2)
    assert riga == {
        "nome": "Tastiera",
        "prezzo_unitario": 50.0,
        "quantita": 2,
        "subtotale": 100.0,
    }


def test_crea_riga_carrello_errori():
    with pytest.raises(ValueError, match="la quantità deve essere maggiore di zero"):
        ecommerce.crea_riga_carrello("Tastiera", 50.0, 0)

    with pytest.raises(ValueError, match="la quantità deve essere maggiore di zero"):
        ecommerce.crea_riga_carrello("Tastiera", 50.0, -1)

    with pytest.raises(ValueError, match="il prezzo unitario non può essere negativo"):
        ecommerce.crea_riga_carrello("Tastiera", -10.0, 1)


def test_calcola_totale_carrello():
    righe = [
        {"subtotale": 10.0},
        {"subtotale": 25.5},
    ]
    assert ecommerce.calcola_totale_carrello(righe) == 35.5
    assert ecommerce.calcola_totale_carrello([]) == 0.0


def test_svuota_articoli_esauriti():
    righe = [
        {"nome": "Mouse", "subtotale": 20.0},
        {"nome": "Cuffie", "subtotale": 50.0},
        {"nome": "Cavo", "subtotale": 5.0},
    ]
    magazzino = {"Mouse": 5, "Cuffie": 0}  # Cavo assente dal magazzino

    risultato = ecommerce.svuota_articoli_esauriti(righe, magazzino)
    assert len(risultato) == 1
    assert risultato[0]["nome"] == "Mouse"


def test_calcola_totale_ordine():
    righe = [
        {"nome": "Mouse", "subtotale": 20.0},
        {"nome": "Cuffie", "subtotale": 50.0},
    ]
    magazzino = {"Mouse": 2, "Cuffie": 0}
    tabella_sconti = {"PROMO10": 10}

    ordine = ecommerce.calcola_totale_ordine(
        righe_carrello=righe,
        magazzino=magazzino,
        codice_sconto="PROMO10",
        tabella_codici=tabella_sconti,
        aliquota_iva=22,
    )

    assert len(ordine["righe_valide"]) == 1
    assert ordine["totale_netto"] == 18.0
    assert ordine["totale_lordo"] == 21.96


# ---------------------------------------------------------------------------
# Test Spedizione
# ---------------------------------------------------------------------------

def test_calcola_costo_spedizione():
    assert ecommerce.calcola_costo_spedizione(10, 100, espressa=False) == 10.0
    assert ecommerce.calcola_costo_spedizione(10, 100, espressa=True) == 20.0


def test_calcola_costo_spedizione_errori():
    with pytest.raises(ValueError, match="peso e distanza non possono essere negativi"):
        ecommerce.calcola_costo_spedizione(-1, 100)

    with pytest.raises(ValueError, match="peso e distanza non possono essere negativi"):
        ecommerce.calcola_costo_spedizione(10, -50)

    with pytest.raises(ValueError, match="peso massimo consentito: 30 kg"):
        ecommerce.calcola_costo_spedizione(31, 100)


def test_stima_data_consegna():
    venerdi = date(2026, 10, 2)
    consegna = ecommerce.stima_data_consegna(venerdi, 2)
    assert consegna == date(2026, 10, 5)

    assert ecommerce.stima_data_consegna(venerdi, 0) == venerdi


def test_stima_data_consegna_errore():
    with pytest.raises(ValueError, match="i giorni lavorativi non possono essere negativi"):
        ecommerce.stima_data_consegna(date(2026, 10, 1), -1)


# ---------------------------------------------------------------------------
# Test Punti Fedeltà e Cliente
# ---------------------------------------------------------------------------

def test_calcola_punti_fedelta():
    assert ecommerce.calcola_punti_fedelta(25.0) == 2
    assert ecommerce.calcola_punti_fedelta(25.0, moltiplicatore=2) == 4
    assert ecommerce.calcola_punti_fedelta(3.0) == 0


def test_calcola_punti_fedelta_errori():
    with pytest.raises(ValueError, match="il totale speso non può essere negativo"):
        ecommerce.calcola_punti_fedelta(-10.0)

    with pytest.raises(ValueError, match="il moltiplicatore deve essere positivo"):
        ecommerce.calcola_punti_fedelta(50.0, moltiplicatore=0)


def test_promuovi_livello_cliente():
    assert ecommerce.promuovi_livello_cliente(50) == "bronze"
    assert ecommerce.promuovi_livello_cliente(100) == "silver"
    assert ecommerce.promuovi_livello_cliente(500) == "gold"
    assert ecommerce.promuovi_livello_cliente(2000) == "platinum"


def test_promuovi_livello_cliente_errore():
    with pytest.raises(ValueError, match="i punti totali non possono essere negativi"):
        ecommerce.promuovi_livello_cliente(-5)


def test_riepilogo_cliente():
    riepilogo = ecommerce.riepilogo_cliente(1500.0, moltiplicatore=1)
    assert riepilogo == {
        "totale_speso": 1500.0,
        "punti": 150,
        "livello": "silver",
    }