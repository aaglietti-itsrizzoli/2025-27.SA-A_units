from datetime import date

import ecommerce
import pytest


def test_calcola_prezzo_scontato_applica_percentuale_e_arrotonda():
    assert ecommerce.calcola_prezzo_scontato(19.99, 15) == 16.99


def test_calcola_prezzo_scontato_gestisce_sconto_zero_e_centopercento():
    assert ecommerce.calcola_prezzo_scontato(12.34, 0) == 12.34
    assert ecommerce.calcola_prezzo_scontato(12.34, 100) == 0


def test_calcola_prezzo_scontato_rifiuta_prezzo_negativo():
    with pytest.raises(ValueError):
        ecommerce.calcola_prezzo_scontato(-1, 10)


@pytest.mark.parametrize("percentuale", [-1, 101])
def test_calcola_prezzo_scontato_rifiuta_percentuale_fuori_intervallo(percentuale):
    with pytest.raises(ValueError):
        ecommerce.calcola_prezzo_scontato(10, percentuale)


def test_applica_codice_sconto_applica_codice_presente():
    assert ecommerce.applica_codice_sconto(80, "ESTATE", {"ESTATE": 25}) == 60


def test_applica_codice_sconto_ignora_codice_inesistente():
    assert ecommerce.applica_codice_sconto(12.34, "SCONOSCIUTO", {}) == 12.34


def test_calcola_iva_applica_aliquota_predefinita():
    assert ecommerce.calcola_iva(100) == 122


def test_calcola_iva_applica_aliquota_personalizzata_e_zero():
    assert ecommerce.calcola_iva(10, 5) == 10.5
    assert ecommerce.calcola_iva(10, 0) == 10


@pytest.mark.parametrize("prezzo, aliquota", [(-1, 22), (10, -1)])
def test_calcola_iva_rifiuta_valori_negativi(prezzo, aliquota):
    with pytest.raises(ValueError):
        ecommerce.calcola_iva(prezzo, aliquota)


def test_crea_riga_carrello_calcola_subtotale():
    assert ecommerce.crea_riga_carrello("Penna", 4.25, 3) == {
        "nome": "Penna",
        "prezzo_unitario": 4.25,
        "quantita": 3,
        "subtotale": 12.75,
    }


def test_crea_riga_carrello_accetta_prezzo_zero():
    assert ecommerce.crea_riga_carrello("Omaggio", 0, 1)["subtotale"] == 0


@pytest.mark.parametrize("quantita", [0, -1])
def test_crea_riga_carrello_rifiuta_quantita_non_positiva(quantita):
    with pytest.raises(ValueError):
        ecommerce.crea_riga_carrello("Penna", 2, quantita)


def test_crea_riga_carrello_rifiuta_prezzo_negativo():
    with pytest.raises(ValueError):
        ecommerce.crea_riga_carrello("Penna", -2, 1)


def test_calcola_totale_carrello_somma_subtotali():
    righe = [{"subtotale": 12.5}, {"subtotale": 3.25}]
    assert ecommerce.calcola_totale_carrello(righe) == 15.75


def test_calcola_totale_carrello_vuoto_restituisce_zero():
    assert ecommerce.calcola_totale_carrello([]) == 0


def test_svuota_articoli_esauriti_filtra_senza_modificare_input():
    righe = [
        {"nome": "Disponibile", "subtotale": 5},
        {"nome": "Esaurito", "subtotale": 7},
        {"nome": "Assente", "subtotale": 9},
    ]
    righe_originali = righe.copy()

    risultato = ecommerce.svuota_articoli_esauriti(
        righe, {"Disponibile": 4, "Esaurito": 0}
    )

    assert risultato == [righe[0]]
    assert righe == righe_originali
    assert risultato is not righe


def test_calcola_totale_ordine_filtra_sconta_e_applica_iva():
    righe = [
        {"nome": "Disponibile", "subtotale": 100},
        {"nome": "Esaurito", "subtotale": 50},
    ]

    risultato = ecommerce.calcola_totale_ordine(
        righe,
        {"Disponibile": 1, "Esaurito": 0},
        "SCONTO",
        {"SCONTO": 10},
        aliquota_iva=10,
    )

    assert risultato == {
        "righe_valide": [righe[0]],
        "totale_netto": 90,
        "totale_lordo": 99,
    }


def test_calcola_totale_ordine_senza_sconto():
    risultato = ecommerce.calcola_totale_ordine(
        [{"nome": "Prodotto", "subtotale": 10}],
        {"Prodotto": 1},
        codice_sconto="SCONTO",
        tabella_codici=None,
    )

    assert risultato["totale_netto"] == 10
    assert risultato["totale_lordo"] == 12.2


def test_calcola_costo_spedizione_calcola_tariffa_standard():
    assert ecommerce.calcola_costo_spedizione(2, 100) == 6


def test_calcola_costo_spedizione_raddoppia_tariffa_espressa():
    assert ecommerce.calcola_costo_spedizione(2, 100, espressa=True) == 12


def test_calcola_costo_spedizione_accetta_limite_massimo():
    assert ecommerce.calcola_costo_spedizione(30, 0) == 18


@pytest.mark.parametrize("peso, distanza", [(-1, 0), (0, -1)])
def test_calcola_costo_spedizione_rifiuta_peso_o_distanza_negativi(peso, distanza):
    with pytest.raises(ValueError):
        ecommerce.calcola_costo_spedizione(peso, distanza)


def test_calcola_costo_spedizione_rifiuta_peso_superiore_al_limite():
    with pytest.raises(ValueError):
        ecommerce.calcola_costo_spedizione(30.01, 0)


def test_stima_data_consegna_salta_fine_settimana():
    assert ecommerce.stima_data_consegna(date(2025, 1, 3), 2) == date(2025, 1, 7)


def test_stima_data_consegna_con_zero_giorni():
    ordine = date(2025, 1, 4)
    assert ecommerce.stima_data_consegna(ordine, 0) == ordine


def test_stima_data_consegna_rifiuta_giorni_negativi():
    with pytest.raises(ValueError):
        ecommerce.stima_data_consegna(date(2025, 1, 1), -1)


def test_calcola_punti_fedelta_zero_punti_per_dieci_euro_acquisto():
    assert ecommerce.calcola_punti_fedelta(3) == 0


def test_calcola_punti_fedelta_usa_soglia_e_moltiplicatore():
    assert ecommerce.calcola_punti_fedelta(29.99) == 2
    assert ecommerce.calcola_punti_fedelta(25, moltiplicatore=3) == 6


def test_calcola_punti_fedelta_rifiuta_spesa_negativa():
    with pytest.raises(ValueError):
        ecommerce.calcola_punti_fedelta(-1)


@pytest.mark.parametrize("moltiplicatore", [0, -1])
def test_calcola_punti_fedelta_rifiuta_moltiplicatore_non_positivo(moltiplicatore):
    with pytest.raises(ValueError):
        ecommerce.calcola_punti_fedelta(10, moltiplicatore)


def test_promuovi_livello_cliente_assegna_livelli_sulle_soglie():
    assert [ecommerce.promuovi_livello_cliente(punti) for punti in (0, 100, 500, 2000)] == [
        "bronze",
        "silver",
        "gold",
        "platinum",
    ]


def test_promuovi_livello_cliente_rifiuta_punti_negativi():
    with pytest.raises(ValueError):
        ecommerce.promuovi_livello_cliente(-1)


def test_riepilogo_cliente_compone_punti_e_livello():
    assert ecommerce.riepilogo_cliente(1000, moltiplicatore=2) == {
        "totale_speso": 1000,
        "punti": 200,
        "livello": "silver",
    }


def test_riepilogo_cliente_rifiuta_spesa_negativa():
    with pytest.raises(ValueError):
        ecommerce.riepilogo_cliente(-1)
