# i tuoi test di unità qua
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

# =============================================================================
# Catalogo e prezzi
# =============================================================================


def test_calcola_prezzo_scontato_valido():
    assert calcola_prezzo_scontato(100.0, 20) == 80.0


def test_calcola_prezzo_scontato_sconto_zero():
    assert calcola_prezzo_scontato(50.0, 0) == 50.0


def test_calcola_prezzo_scontato_sconto_totale():
    assert calcola_prezzo_scontato(50.0, 100) == 0.0


def test_calcola_prezzo_scontato_prezzo_negativo_solleva_errore():
    with pytest.raises(ValueError, match="il prezzo non può essere negativo"):
        calcola_prezzo_scontato(-10.0, 10)


def test_calcola_prezzo_scontato_percentuale_non_valida_solleva_errore():
    with pytest.raises(
        ValueError, match="la percentuale di sconto deve essere tra 0 e 100"
    ):
        calcola_prezzo_scontato(100.0, 150)

    with pytest.raises(
        ValueError, match="la percentuale di sconto deve essere tra 0 e 100"
    ):
        calcola_prezzo_scontato(100.0, -5)


def test_applica_codice_sconto_esistente():
    tabella = {"ESTATE20": 20, "BLACKFRIDAY": 50}
    assert applica_codice_sconto(100.0, "ESTATE20", tabella) == 80.0


def test_applica_codice_sconto_non_esistente():
    tabella = {"ESTATE20": 20}
    assert applica_codice_sconto(100.0, "NON_ESISTE", tabella) == 100.0


def test_calcola_iva_default():
    assert calcola_iva(100.0) == 122.0


def test_calcola_iva_aliquota_personalizzata():
    assert calcola_iva(100.0, 10) == 110.0


def test_calcola_iva_prezzo_negativo_solleva_errore():
    with pytest.raises(
        ValueError, match="il prezzo netto non può essere negativo"
    ):
        calcola_iva(-50.0)


def test_calcola_iva_aliquota_negativa_solleva_errore():
    with pytest.raises(ValueError, match="l'aliquota non può essere negativa"):
        calcola_iva(100.0, -5)


# =============================================================================
# Carrello
# =============================================================================


def test_crea_riga_carrello_valida():
    riga = crea_riga_carrello("Mouse", 25.0, 2)
    assert riga == {
        "nome": "Mouse",
        "prezzo_unitario": 25.0,
        "quantita": 2,
        "subtotale": 50.0,
    }


def test_crea_riga_carrello_quantita_non_valida_solleva_errore():
    with pytest.raises(
        ValueError, match="la quantità deve essere maggiore di zero"
    ):
        crea_riga_carrello("Tastiera", 50.0, 0)

    with pytest.raises(
        ValueError, match="la quantità deve essere maggiore di zero"
    ):
        crea_riga_carrello("Tastiera", 50.0, -1)


def test_crea_riga_carrello_prezzo_negativo_solleva_errore():
    with pytest.raises(
        ValueError, match="il prezzo unitario non può essere negativo"
    ):
        crea_riga_carrello("Monitor", -100.0, 1)


def test_calcola_totale_carrello_con_righe():
    righe = [
        {"nome": "A", "prezzo_unitario": 25.0, "quantita": 1, "subtotale": 25.0},
        {
            "nome": "B",
            "prezzo_unitario": 15.5,
            "quantita": 1,
            "subtotale": 15.5,
        },
    ]
    assert calcola_totale_carrello(righe) == 40.5


def test_calcola_totale_carrello_vuoto():
    assert calcola_totale_carrello([]) == 0.0


def test_svuota_articoli_esauriti():
    righe = [
        {"nome": "ProdottoA", "subtotale": 10.0},
        {"nome": "ProdottoB", "subtotale": 20.0},
        {"nome": "ProdottoC", "subtotale": 30.0},
    ]
    magazzino = {"ProdottoA": 5, "ProdottoB": 0}

    risultato = svuota_articoli_esauriti(righe, magazzino)

    assert len(risultato) == 1
    assert risultato[0]["nome"] == "ProdottoA"
    assert len(righe) == 3  # Verifica immutabilità della lista originale


def test_calcola_totale_ordine_completo():
    righe = [
        {"nome": "ProdottoA", "subtotale": 100.0},
        {"nome": "ProdottoB", "subtotale": 50.0},
    ]
    magazzino = {"ProdottoA": 10, "ProdottoB": 0}  # ProdottoB viene scartato
    tabella_codici = {"PROMO10": 10}

    ordine = calcola_totale_ordine(
        righe_carrello=righe,
        magazzino=magazzino,
        codice_sconto="PROMO10",
        tabella_codici=tabella_codici,
        aliquota_iva=22,
    )

    assert len(ordine["righe_valide"]) == 1
    assert ordine["totale_netto"] == 90.0  # 100.0 - 10%
    assert ordine["totale_lordo"] == 109.8  # 90.0 * 1.22


# =============================================================================
# Spedizione
# =============================================================================


def test_calcola_costo_spedizione_standard():
    # Costo = 3.0 + (0.5 * 5) + (0.02 * 100) = 3.0 + 2.5 + 2.0 = 7.5
    assert calcola_costo_spedizione(peso_kg=5.0, distanza_km=100.0) == 7.5


def test_calcola_costo_spedizione_espressa():
    # Costo = (3.0 + 2.5 + 2.0) * 2 = 15.0
    assert (
        calcola_costo_spedizione(
            peso_kg=5.0, distanza_km=100.0, espressa=True
        )
        == 15.0
    )


def test_calcola_costo_spedizione_peso_eccessivo_solleva_errore():
    with pytest.raises(ValueError, match="peso massimo consentito: 30 kg"):
        calcola_costo_spedizione(peso_kg=35.0, distanza_km=10.0)


def test_calcola_costo_spedizione_parametri_negativi_solleva_errore():
    with pytest.raises(
        ValueError, match="peso e distanza non possono essere negativi"
    ):
        calcola_costo_spedizione(peso_kg=-1.0, distanza_km=10.0)

    with pytest.raises(
        ValueError, match="peso e distanza non possono essere negativi"
    ):
        calcola_costo_spedizione(peso_kg=5.0, distanza_km=-10.0)


def test_stima_data_consegna_senza_weekend():
    lunedì = date(2026, 3, 2)
    # 3 giorni lavorativi: Martedì, Mercoledì, Giovedì (2026-03-05)
    assert stima_data_consegna(lunedì, 3) == date(2026, 3, 5)


def test_stima_data_consegna_con_weekend():
    giovedì = date(2026, 3, 5)
    # 3 giorni lavorativi: Venerdì (1), Lunedì (2), Martedì (3) -> 2026-03-10
    assert stima_data_consegna(giovedì, 3) == date(2026, 3, 10)


def test_stima_data_consegna_giorni_negativi_solleva_errore():
    with pytest.raises(
        ValueError, match="i giorni lavorativi non possono essere negativi"
    ):
        stima_data_consegna(date(2026, 3, 2), -1)


# =============================================================================
# Fedeltà cliente / punti
# =============================================================================


def test_calcola_punti_fedelta_zero_punti_per_dieci_euro_acquisto():
    assert calcola_punti_fedelta(3.0) == 0


def test_calcola_punti_fedelta_con_moltiplicatore():
    # 25 // 10 = 2 punti base. Con moltiplicatore 2 -> 4 punti.
    assert calcola_punti_fedelta(25.0, moltiplicatore=2) == 4


def test_calcola_punti_fedelta_parametri_non_validi_solleva_errore():
    with pytest.raises(
        ValueError, match="il totale speso non può essere negativo"
    ):
        calcola_punti_fedelta(-10.0)

    with pytest.raises(
        ValueError, match="il moltiplicatore deve essere positivo"
    ):
        calcola_punti_fedelta(50.0, moltiplicatore=0)


@pytest.mark.parametrize(
    "punti, livello_atteso",
    [
        (0, "bronze"),
        (99, "bronze"),
        (100, "silver"),
        (499, "silver"),
        (500, "gold"),
        (1999, "gold"),
        (2000, "platinum"),
    ],
)
def test_promuovi_livello_cliente_soglie(punti, livello_atteso):
    assert promuovi_livello_cliente(punti) == livello_atteso


def test_promuovi_livello_cliente_punti_negativi_solleva_errore():
    with pytest.raises(
        ValueError, match="i punti totali non possono essere negativi"
    ):
        promuovi_livello_cliente(-5)


def test_riepilogo_cliente_completo():
    riepilogo = riepilogo_cliente(150.0)
    assert riepilogo == {
        "totale_speso": 150.0,
        "punti": 15,
        "livello": "bronze",
    }
