# i tuoi test di unità qua
import ecommerce
import pytest

def test_calcola_punti_fedelta_zero_punti_per_dieci_euro_acquisto():
    assert ecommerce.calcola_punti_fedelta(3) == 0


def test_calcola_spedizione_se_cliente_non_decide_fra_spedizione_espressa_o_ordinaria():
    peso_kg = 15
    distanza_km = 50

    risultato = ecommerce.calcola_costo_spedizione(peso_kg, distanza_km)

    assert risultato == round(3.0 + 0.5 * peso_kg + 0.02 * distanza_km, 2)

def test_calcola_sconto_valore_oltre_cento():
    with pytest.raises(ValueError):
        ecommerce.calcola_prezzo_scontato(200, 500)

def test_riepilogo_cliente_saldo_negativo():
    with pytest.raises(ValueError):
        ecommerce.riepilogo_cliente(-5)


def test_riepilogo_cliente_saldo_positivo():
    riepilogo = ecommerce.riepilogo_cliente(1752.25)

    assert riepilogo["totale_speso"] == 1752.25
    assert riepilogo["punti"] == 175
    assert riepilogo["livello"] == "silver"