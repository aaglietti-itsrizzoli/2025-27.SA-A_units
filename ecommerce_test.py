import pytest
from ecommerce import (
    calcola_punti_fedelta,
    crea_riga_carrello,
    calcola_totale_carrello
)


# ==============================================================================
# SCENARIO 1: Calcolo Punti Fedeltà (5 varianti con input diversi)
# ==============================================================================

def test_calcola_punti_fedelta_zero_punti_per_dieci_euro_acquisto():
    # Given: un acquisto di 3 euro
    importo = 3
    
    # When: un cliente conclude un acquisto fn:calcola_punti_fedelta ne calcola i punti fedeltà
    punti = calcola_punti_fedelta(importo)
    
    # Then: il cliente riceve 0 punti fedeltà perchè l'acquisto è inferiore a 10 euro
    assert punti == 0


def test_calcola_punti_fedelta_limite_inferiore_nove_euro_e_novantanove():
    # Given: un acquisto di 9.99 euro
    importo = 9.99
    
    # When: si calcolano i punti fedeltà
    punti = calcola_punti_fedelta(importo)
    
    # Then: i punti devono essere ancora 0
    assert punti == 0


def test_calcola_punti_fedelta_soglia_esatta_dieci_euro():
    # Given: un acquisto di 10 euro
    importo = 10.0
    
    # When: si calcolano i punti fedeltà
    punti = calcola_punti_fedelta(importo)
    
    # Then: il cliente ottiene 1 punto fedeltà
    assert punti == 1


def test_calcola_punti_fedelta_acquisto_cinquanta_euro():
    # Given: un acquisto di 55.50 euro
    importo = 55.50
    
    # When: si calcolano i punti fedeltà
    punti = calcola_punti_fedelta(importo)
    
    # Then: il cliente riceve 5 punti fedeltà (1 punto ogni 10 euro interi)
    assert punti == 5


def test_calcola_punti_fedelta_grande_acquisto():
    # Given: un acquisto di 250 euro
    importo = 250.0
    
    # When: si calcolano i punti fedeltà
    punti = calcola_punti_fedelta(importo)
    
    # Then: il cliente riceve 25 punti fedeltà
    assert punti == 25


# ==============================================================================
# SCENARIO 2: Calcolo Totale Carrello (5 varianti con input diversi)
# ==============================================================================

def test_calcola_totale_carrello_per_20_oggetti():
    # Given: 20 oggetti (ognuno con nome, prezzo_unitario, quantita)
    carrello = []
    for i in range(1, 21):
        riga = crea_riga_carrello(f"Prodotto_{i}", prezzo_unitario=10.0, quantita=1)
        carrello.append(riga)
    
    # When: fn:calcola_totale_carrello ne calcola il totale
    totale = calcola_totale_carrello(carrello)
    
    # Then: il totale deve essere 200.0 euro (20 articoli x 10.0)
    assert totale == pytest.approx(200.0)


def test_calcola_totale_carrello_singolo_prodotto():
    # Given: 1 prodotto nel carrello (prezzo 15.50, quantità 2)
    carrello = [crea_riga_carrello("Libro", prezzo_unitario=15.50, quantita=2)]
    
    # When: si calcola il totale del carrello
    totale = calcola_totale_carrello(carrello)
    
    # Then: il totale deve essere 31.0 euro
    assert totale == pytest.approx(31.0)


def test_calcola_totale_carrello_prodotti_misti():
    # Given: 3 oggetti differenti con quantità e prezzi differenti
    carrello = [
        crea_riga_carrello("Tastiera", prezzo_unitario=49.99, quantita=1),
        crea_riga_carrello("Mouse", prezzo_unitario=19.50, quantita=2),
        crea_riga_carrello("Cavo HDMI", prezzo_unitario=5.00, quantita=3)
    ]
    
    # When: si calcola il totale del carrello
    totale = calcola_totale_carrello(carrello)
    
    # Then: totale = 49.99 + (19.50 * 2) + (5.00 * 3) = 103.99
    assert totale == pytest.approx(103.99)


def test_calcola_totale_carrello_vuoto():
    # Given: un carrello senza oggetti
    carrello = []
    
    # When: si calcola il totale del carrello
    totale = calcola_totale_carrello(carrello)
    
    # Then: il totale deve essere 0.0 euro
    assert totale == 0.0


def test_calcola_totale_carrello_con_quantita_zero():
    # Given: prodotti aggiunti ma con quantità pari a 0
    carrello = [
        crea_riga_carrello("Monitor", prezzo_unitario=150.0, quantita=0),
        crea_riga_carrello("Cuffie", prezzo_unitario=30.0, quantita=1)
    ]
    
    # When: si calcola il totale del carrello
    totale = calcola_totale_carrello(carrello)
    
    # Then: il totale deve considerare solo i prodotti acquistati (30.0 euro)
    assert totale == pytest.approx(30.0)