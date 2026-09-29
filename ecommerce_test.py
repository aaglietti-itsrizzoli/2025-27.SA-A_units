from datetime import date

import pytest

import ecommerce


def test_calcolo_del_totale_con_carrello_vuoto():
    ordine = ecommerce.calcola_totale_ordine([], {})

    assert ordine["totale_lordo"] == 0.00
    assert "costo_spedizione" not in ordine


def test_aggiunta_di_prodotti_validi_al_carrello():
    carrello = [
        ecommerce.crea_riga_carrello("Laptop", 1000.00, 1),
        ecommerce.crea_riga_carrello("Mouse", 25.00, 2),
    ]

    assert len(carrello) == 2
    assert ecommerce.calcola_totale_carrello(carrello) == 1050.00


def test_applicazione_di_un_codice_sconto_percentuale_valido():
    totale_scontato = ecommerce.applica_codice_sconto(
        100.00, "SUMMER10", {"SUMMER10": 10}
    )

    assert totale_scontato == 90.00


def test_inserimento_di_un_prodotto_con_prezzo_o_quantita_non_validi():
    import pytest

    with pytest.raises(ValueError):
        ecommerce.crea_riga_carrello("Prodotto", -10.00, 1)

    with pytest.raises(ValueError):
        ecommerce.crea_riga_carrello("Prodotto", 10.00, 0)


def test_rimozione_di_un_prodotto_dal_carrello():
    carrello = [ecommerce.crea_riga_carrello("Tastiera", 50.00, 1)]

    carrello = ecommerce.svuota_articoli_esauriti(carrello, {})

    assert carrello == []


def test_applicazione_della_spedizione_gratuita_sopra_una_soglia():
    carrello = [ecommerce.crea_riga_carrello("Prodotto", 60.00, 1)]
    ordine = ecommerce.calcola_totale_ordine(
        carrello, {"Prodotto": 1}, aliquota_iva=0
    )

    assert ordine["totale_lordo"] == 60.00
    assert "costo_spedizione" not in ordine


@pytest.mark.parametrize(
    ("prezzo", "sconto", "atteso"),
    [(100, 0, 100), (100, 10, 90), (25, 100, 0)],
)
def test_calcola_prezzo_scontato(prezzo, sconto, atteso):
    assert ecommerce.calcola_prezzo_scontato(prezzo, sconto) == atteso


@pytest.mark.parametrize(
    ("prezzo", "sconto"),
    [(-1, 0), (10, -1), (10, 101)],
)
def test_calcola_prezzo_scontato_rifiuta_valori_non_validi(prezzo, sconto):
    with pytest.raises(ValueError):
        ecommerce.calcola_prezzo_scontato(prezzo, sconto)


def test_codice_sconto_inesistente_non_applica_sconti():
    assert ecommerce.applica_codice_sconto(42.50, "SCONOSCIUTO", {}) == 42.50


@pytest.mark.parametrize(
    ("prezzo", "aliquota", "atteso"),
    [(100, 22, 122), (100, 10, 110), (0, 22, 0)],
)
def test_calcola_iva(prezzo, aliquota, atteso):
    assert ecommerce.calcola_iva(prezzo, aliquota) == atteso


@pytest.mark.parametrize(("prezzo", "aliquota"), [(-1, 22), (10, -1)])
def test_calcola_iva_rifiuta_valori_non_validi(prezzo, aliquota):
    with pytest.raises(ValueError):
        ecommerce.calcola_iva(prezzo, aliquota)


def test_svuota_articoli_esauriti_conserva_prodotti_disponibili():
    carrello = [
        ecommerce.crea_riga_carrello("Disponibile", 10, 1),
        ecommerce.crea_riga_carrello("Esaurito", 20, 1),
    ]

    righe_valide = ecommerce.svuota_articoli_esauriti(
        carrello, {"Disponibile": 3, "Esaurito": 0}
    )

    assert [riga["nome"] for riga in righe_valide] == ["Disponibile"]
    assert len(carrello) == 2


def test_totale_ordine_applica_sconto_e_iva_sulle_righe_disponibili():
    carrello = [
        ecommerce.crea_riga_carrello("Disponibile", 50, 2),
        ecommerce.crea_riga_carrello("Esaurito", 100, 1),
    ]

    ordine = ecommerce.calcola_totale_ordine(
        carrello,
        {"Disponibile": 5, "Esaurito": 0},
        codice_sconto="SCONTO10",
        tabella_codici={"SCONTO10": 10},
    )

    assert len(ordine["righe_valide"]) == 1
    assert ordine["totale_netto"] == 90
    assert ordine["totale_lordo"] == 109.8


def test_calcola_costo_spedizione_standard_ed_espressa():
    assert ecommerce.calcola_costo_spedizione(1, 100) == 5.5
    assert ecommerce.calcola_costo_spedizione(1, 100, espressa=True) == 11.0


@pytest.mark.parametrize(("peso", "distanza"), [(-1, 10), (1, -10), (31, 0)])
def test_calcola_costo_spedizione_rifiuta_valori_non_validi(peso, distanza):
    with pytest.raises(ValueError):
        ecommerce.calcola_costo_spedizione(peso, distanza)


def test_stima_data_consegna_salva_i_fine_settimana():
    venerdi = date(2024, 3, 1)

    assert ecommerce.stima_data_consegna(venerdi, 0) == venerdi
    assert ecommerce.stima_data_consegna(venerdi, 1) == date(2024, 3, 4)


def test_stima_data_consegna_rifiuta_giorni_negativi():
    with pytest.raises(ValueError):
        ecommerce.stima_data_consegna(date(2024, 3, 1), -1)


@pytest.mark.parametrize(("totale", "moltiplicatore", "atteso"), [(0, 1, 0), (39, 2, 6)])
def test_calcola_punti_fedelta(totale, moltiplicatore, atteso):
    assert ecommerce.calcola_punti_fedelta(totale, moltiplicatore) == atteso


@pytest.mark.parametrize(("totale", "moltiplicatore"), [(-1, 1), (10, 0)])
def test_calcola_punti_fedelta_rifiuta_valori_non_validi(totale, moltiplicatore):
    with pytest.raises(ValueError):
        ecommerce.calcola_punti_fedelta(totale, moltiplicatore)


@pytest.mark.parametrize(
    ("punti", "livello"),
    [(0, "bronze"), (100, "silver"), (500, "gold"), (2000, "platinum")],
)
def test_promuovi_livello_cliente(punti, livello):
    assert ecommerce.promuovi_livello_cliente(punti) == livello


def test_promuovi_livello_cliente_rifiuta_punti_negativi():
    with pytest.raises(ValueError):
        ecommerce.promuovi_livello_cliente(-1)


def test_riepilogo_cliente():
    assert ecommerce.riepilogo_cliente(1000) == {
        "totale_speso": 1000,
        "punti": 100,
        "livello": "silver",
    }
