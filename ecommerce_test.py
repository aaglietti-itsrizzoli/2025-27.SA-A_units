import pytest
from ecommerce import calcola_punti_fedelta, calcola_prezzo_scontato

def test_calcola_punti_fedelta_zero_punti_per_dieci_euro_acquisto():
    # Given: un acquisto di 3 euro
    acquisto = 3.0
    
    # When: si calcolano i punti fedeltà
    punti = calcola_punti_fedelta(acquisto)
    
    # Then: il cliente riceve 0 punti (acquisto inferiore a 10 euro)
    assert punti == 0

def test_applicazione_di_uno_sconto_valido_su_un_prezzo_positivo():
    # Given: un prezzo iniziale di 100.0 e uno sconto del 20%
    prezzo_iniziale = 100.0
    sconto = 20.0
    
    # When: calcolo il prezzo scontato
    prezzo_finale = calcola_prezzo_scontato(prezzo_iniziale, sconto)
    
    # Then: il risultato deve essere 80.0
    assert prezzo_finale == 80.0

def test_errore_se_il_prezzo_negativo():
    # Given: un prezzo iniziale di -10.0 e uno sconto del 20%
    prezzo_iniziale = -10.0
    sconto = 20.0
    
    # When / Then: deve essere sollevata un'eccezione ValueError
    with pytest.raises(ValueError):
        calcola_prezzo_scontato(prezzo_iniziale, sconto)

def test_errore_se_lo_sconto_è_fuori_range():
    # Given: un prezzo iniziale di 50.0 e uno sconto del 110%
    prezzo_iniziale = 50.0
    sconto = 110.0
    
    # When / Then: deve essere sollevata un'eccezione ValueError
    with pytest.raises(ValueError):
        calcola_prezzo_scontato(prezzo_iniziale, sconto)