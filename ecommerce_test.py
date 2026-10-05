import pytest
from ecommerce import (
    calcola_punti_fedelta,
    calcola_prezzo_scontato,
    applica_codice_sconto,
    calcola_iva,
    crea_riga_carrello,
    svuota_articoli_esauriti,
)


# 0 Punti fedeltà
def test_calcola_punti_fedelta_zero_punti_per_dieci_euro_acquisto():
    assert calcola_punti_fedelta(3) == 0


# 1 Sconto su prezzo
def test_calcolo_prezzo_scontato_sopra_100():
    with pytest.raises(
        ValueError, match="la percentuale di sconto deve essere tra 0 e 100"
    ):
        calcola_prezzo_scontato(80, 1000)


def test_calcolo_prezzo_scontato_prezzo_negativo():
    with pytest.raises(ValueError, match="il prezzo non può essere negativo"):
        calcola_prezzo_scontato(-80, 10)


def test_applica_codice_sconto_non_trovato():
    prezzo = 120
    chiave = 10
    dizionario = {1: 10, 2: 15}
    assert applica_codice_sconto(prezzo, chiave, dizionario) == 120


# 3 Calcolo di IVA su prezzo
def test_calcola_iva_prezzo_negativo():
    with pytest.raises(
        ValueError, match="il prezzo netto non può essere negativo"
    ):
        calcola_iva(-50, 20)


def test_calcola_iva_aliquota_negativa():
    with pytest.raises(ValueError, match="l'aliquota non può essere negativa"):
        calcola_iva(50, -20)


# 4 Modifiche delle righe del carrello
def test_crea_riga_carrello_prezzo_non_valido():
    with pytest.raises(
        ValueError, match="il prezzo unitario non può essere negativo"
    ):
        crea_riga_carrello("Cola", -1, 300)


def test_crea_riga_carrello_quantita_non_valida():
    with pytest.raises(
        ValueError, match="la quantità deve essere maggiore di zero"
    ):
        crea_riga_carrello("Cola", 10, -1)


def test_svuota_articoli_esauriti_articoli_presenti():
    prezzo_unitario = 30
    quantita = 2
    righe_carrello = [
        {
            "nome": "Sushi",
            "prezzo_unitario": prezzo_unitario,
            "quantita": quantita,
            "subtotale": round(prezzo_unitario * quantita, 2),
        }
    ]
    magazzino = {"Sushi": 5}

    risultato = svuota_articoli_esauriti(righe_carrello, magazzino)
    assert risultato == righe_carrello


def test_svuota_articoli_esauriti_articoli_non_sufficenti():
    prezzo_unitario = 30
    quantita = 2
    righe_carrello = [
        {
            "nome": "Sushi",
            "prezzo_unitario": prezzo_unitario,
            "quantita": quantita,
            "subtotale": round(prezzo_unitario * quantita, 2),
        }
    ]
    magazzino = {"Sushi": 0}

    risultato = svuota_articoli_esauriti(righe_carrello, magazzino)
    assert risultato == []