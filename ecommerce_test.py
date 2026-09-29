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


# --- Test Punti Fedeltà e Livello ---

def test_calcola_punti_fedelta_zero_punti_per_dieci_euro_acquisto():
    assert calcola_punti_fedelta(3) == 0


def test_calcola_punti_fedelta_validi():
    assert calcola_punti_fedelta(25, 2) == 4


def test_calcola_punti_fedelta_eccezioni():
    with pytest.raises(ValueError):
        calcola_punti_fedelta(-10)
    with pytest.raises(ValueError):
        calcola_punti_fedelta(50, 0)


def test_promuovi_livello_cliente():
    assert promuovi_livello_cliente(50) == "bronze"
    assert promuovi_livello_cliente(150) == "silver"
    assert promuovi_livello_cliente(600) == "gold"
    assert promuovi_livello_cliente(2500) == "platinum"
    with pytest.raises(ValueError):
        promuovi_livello_cliente(-1)


def test_riepilogo_cliente():
    res = riepilogo_cliente(150.0, 2)
    assert res["totale_speso"] == 150.0
    assert res["punti"] == 30
    assert res["livello"] == "bronze"


# --- Test Catalogo e Prezzi ---

def test_calcola_prezzo_scontato_valido():
    assert calcola_prezzo_scontato(100, 20) == 80.0


def test_calcola_prezzo_scontato_eccezioni():
    with pytest.raises(ValueError):
        calcola_prezzo_scontato(-10, 20)
    with pytest.raises(ValueError):
        calcola_prezzo_scontato(100, 150)


def test_applica_codice_sconto():
    tabella = {"PROMO10": 10}
    assert applica_codice_sconto(100, "PROMO10", tabella) == 90.0
    assert applica_codice_sconto(100, "NOCODE", tabella) == 100.0


def test_calcola_iva():
    assert calcola_iva(100) == 122.0
    assert calcola_iva(100, 10) == 110.0
    with pytest.raises(ValueError):
        calcola_iva(-50)
    with pytest.raises(ValueError):
        calcola_iva(100, -10)


# --- Test Carrello ---

def test_crea_riga_carrello():
    riga = crea_riga_carrello("Libro", 15.0, 2)
    assert riga["subtotale"] == 30.0
    with pytest.raises(ValueError):
        crea_riga_carrello("Libro", 15.0, 0)
    with pytest.raises(ValueError):
        crea_riga_carrello("Libro", -5.0, 1)


def test_calcola_totale_carrello():
    carrello = [{"subtotale": 10.0}, {"subtotale": 15.5}]
    assert calcola_totale_carrello(carrello) == 25.5
    assert calcola_totale_carrello([]) == 0


def test_svuota_articoli_esauriti():
    carrello = [{"nome": "Mouse"}, {"nome": "Tastiera"}]
    magazzino = {"Mouse": 5, "Tastiera": 0}
    risultato = svuota_articoli_esauriti(carrello, magazzino)
    assert len(risultato) == 1
    assert risultato[0]["nome"] == "Mouse"


def test_calcola_totale_ordine():
    carrello = [{"nome": "Mouse", "subtotale": 20.0}]
    magazzino = {"Mouse": 5}
    codici = {"PROMO10": 10}
    ordine = calcola_totale_ordine(carrello, magazzino, "PROMO10", codici)
    assert ordine["totale_netto"] == 18.0
    assert ordine["totale_lordo"] == 21.96


# --- Test Spedizione ---

def test_calcola_costo_spedizione():
    assert calcola_costo_spedizione(2, 100) == 6.0
    assert calcola_costo_spedizione(2, 100, espressa=True) == 12.0
    with pytest.raises(ValueError):
        calcola_costo_spedizione(-1, 50)
    with pytest.raises(ValueError):
        calcola_costo_spedizione(35, 50)


def test_stima_data_consegna():
    venerdi = date(2026, 10, 2)
    assert stima_data_consegna(venerdi, 1) == date(2026, 10, 5)
    with pytest.raises(ValueError):
        stima_data_consegna(venerdi, -1)