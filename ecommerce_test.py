from datetime import date

import pytest

import ecommerce


def test_calcola_punti_fedelta_zero_punti_per_dieci_euro_acquisto():
    assert ecommerce.calcola_punti_fedelta(3) == 0


@pytest.mark.parametrize(
    "prezzo, sconto, atteso",
    [(100, 20, 80), (10, 0, 10), (10, 100, 0)],
)
def test_calcola_prezzo_scontato(prezzo, sconto, atteso):
    assert ecommerce.calcola_prezzo_scontato(prezzo, sconto) == atteso


@pytest.mark.parametrize("prezzo, sconto", [(-1, 10), (10, -1), (10, 101)])
def test_calcola_prezzo_scontato_rifiuta_valori_non_validi(prezzo, sconto):
    with pytest.raises(ValueError):
        ecommerce.calcola_prezzo_scontato(prezzo, sconto)


def test_applica_codice_sconto():
    codici = {"PROMO": 25}
    assert ecommerce.applica_codice_sconto(80, "PROMO", codici) == 60
    assert ecommerce.applica_codice_sconto(80, "INESISTENTE", codici) == 80


def test_calcola_iva():
    assert ecommerce.calcola_iva(100) == 122
    assert ecommerce.calcola_iva(100, 10) == 110


@pytest.mark.parametrize("prezzo, aliquota", [(-1, 22), (10, -1)])
def test_calcola_iva_rifiuta_valori_negativi(prezzo, aliquota):
    with pytest.raises(ValueError):
        ecommerce.calcola_iva(prezzo, aliquota)


def test_crea_riga_carrello():
    assert ecommerce.crea_riga_carrello("Libro", 12.50, 2) == {
        "nome": "Libro",
        "prezzo_unitario": 12.50,
        "quantita": 2,
        "subtotale": 25.00,
    }


@pytest.mark.parametrize("prezzo, quantita", [(-1, 1), (10, 0), (10, -1)])
def test_crea_riga_carrello_rifiuta_valori_non_validi(prezzo, quantita):
    with pytest.raises(ValueError):
        ecommerce.crea_riga_carrello("Libro", prezzo, quantita)


def test_calcola_totale_carrello():
    righe = [
        ecommerce.crea_riga_carrello("A", 10, 2),
        ecommerce.crea_riga_carrello("B", 3.50, 1),
    ]
    assert ecommerce.calcola_totale_carrello(righe) == 23.50
    assert ecommerce.calcola_totale_carrello([]) == 0


def test_svuota_articoli_esauriti_non_modifica_lista_input():
    righe = [
        ecommerce.crea_riga_carrello("disponibile", 10, 1),
        ecommerce.crea_riga_carrello("esaurito", 5, 1),
        ecommerce.crea_riga_carrello("assente", 2, 1),
    ]
    risultato = ecommerce.svuota_articoli_esauriti(
        righe, {"disponibile": 3, "esaurito": 0}
    )
    assert risultato == [righe[0]]
    assert risultato is not righe


def test_calcola_totale_ordine_con_sconto_e_articoli_esauriti():
    righe = [
        ecommerce.crea_riga_carrello("disponibile", 50, 2),
        ecommerce.crea_riga_carrello("esaurito", 100, 1),
    ]
    risultato = ecommerce.calcola_totale_ordine(
        righe, {"disponibile": 1, "esaurito": 0}, "PROMO", {"PROMO": 10}
    )
    assert risultato == {
        "righe_valide": [righe[0]],
        "totale_netto": 90,
        "totale_lordo": 109.80,
    }


def test_calcola_totale_ordine_senza_codice_sconto():
    riga = ecommerce.crea_riga_carrello("A", 10, 1)
    risultato = ecommerce.calcola_totale_ordine([riga], {"A": 1})
    assert risultato["totale_netto"] == 10
    assert risultato["totale_lordo"] == 12.20


@pytest.mark.parametrize(
    "peso, distanza, espressa, atteso",
    [(2, 100, False, 6.0), (2, 100, True, 12.0), (30, 0, False, 18.0)],
)
def test_calcola_costo_spedizione(peso, distanza, espressa, atteso):
    assert ecommerce.calcola_costo_spedizione(peso, distanza, espressa) == atteso


@pytest.mark.parametrize("peso, distanza", [(-1, 10), (1, -1), (31, 0)])
def test_calcola_costo_spedizione_rifiuta_valori_non_validi(peso, distanza):
    with pytest.raises(ValueError):
        ecommerce.calcola_costo_spedizione(peso, distanza)


def test_stima_data_consegna_salva_i_weekend():
    venerdi = date(2026, 9, 25)
    assert ecommerce.stima_data_consegna(venerdi, 1) == date(2026, 9, 28)
    assert ecommerce.stima_data_consegna(venerdi, 0) == venerdi


def test_stima_data_consegna_rifiuta_giorni_negativi():
    with pytest.raises(ValueError):
        ecommerce.stima_data_consegna(date(2026, 9, 25), -1)


def test_calcola_punti_fedelta_applica_moltiplicatore():
    assert ecommerce.calcola_punti_fedelta(99.99) == 9
    assert ecommerce.calcola_punti_fedelta(25, 3) == 6


@pytest.mark.parametrize("totale, moltiplicatore", [(-1, 1), (10, 0)])
def test_calcola_punti_fedelta_rifiuta_valori_non_validi(
    totale, moltiplicatore
):
    with pytest.raises(ValueError):
        ecommerce.calcola_punti_fedelta(totale, moltiplicatore)



