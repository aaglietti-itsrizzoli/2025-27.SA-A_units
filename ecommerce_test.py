from ecommerce import calcola_punti_fedelta

# --- ACQUISTI SOTTO I 10 EURO (0 PUNTI) ---

def test_calcola_punti_fedelta_zero_euro():
    # Given
    importo_acquisto = 0
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_un_centesimo():
    # Given
    importo_acquisto = 0.01
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_un_euro():
    # Given
    importo_acquisto = 1
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_due_euro():
    # Given
    importo_acquisto = 2
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_tre_euro():
    # Given
    importo_acquisto = 3
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_quattro_euro():
    # Given
    importo_acquisto = 4
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_cinque_euro():
    # Given
    importo_acquisto = 5
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_cinque_euro_cinquanta():
    # Given
    importo_acquisto = 5.50
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_sette_euro_novantanove():
    # Given
    importo_acquisto = 7.99
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_nove_euro():
    # Given
    importo_acquisto = 9
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_limite_inferiore_dieci_euro():
    # Given
    importo_acquisto = 9.99
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0


# --- ACQUISTI TRA 10 E 19 EURO (1 PUNTO) ---

def test_calcola_punti_fedelta_esattamente_dieci_euro():
    # Given
    importo_acquisto = 10
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 1

def test_calcola_punti_fedelta_dieci_euro_un_centesimo():
    # Given
    importo_acquisto = 10.01
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 1

def test_calcola_punti_fedelta_dodici_euro():
    # Given
    importo_acquisto = 12
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 1

def test_calcola_punti_fedelta_quindici_euro():
    # Given
    importo_acquisto = 15
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 1

def test_calcola_punti_fedelta_diciotto_euro():
    # Given
    importo_acquisto = 18
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 1

def test_calcola_punti_fedelta_limite_inferiore_venti_euro():
    # Given
    importo_acquisto = 19.99
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 1


# --- ACQUISTI TRA 20 E 99 EURO ---

def test_calcola_punti_fedelta_esattamente_venti_euro():
    # Given
    importo_acquisto = 20
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 2

def test_calcola_punti_fedelta_venti_euro_cinquanta():
    # Given
    importo_acquisto = 20.50
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 2

def test_calcola_punti_fedelta_venticinque_euro():
    # Given
    importo_acquisto = 25
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 2

def test_calcola_punti_fedelta_ventinove_euro_novantanove():
    # Given
    importo_acquisto = 29.99
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 2

def test_calcola_punti_fedelta_trenta_euro():
    # Given
    importo_acquisto = 30
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 3

def test_calcola_punti_fedelta_trentatre_euro():
    # Given
    importo_acquisto = 33
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 3

def test_calcola_punti_fedelta_quaranta_euro():
    # Given
    importo_acquisto = 40
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 4

def test_calcola_punti_fedelta_quarantanove_euro_novantanove():
    # Given
    importo_acquisto = 49.99
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 4

def test_calcola_punti_fedelta_cinquanta_euro():
    # Given
    importo_acquisto = 50
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 5

def test_calcola_punti_fedelta_sessanta_euro():
    # Given
    importo_acquisto = 60
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 6

def test_calcola_punti_fedelta_settanta_euro():
    # Given
    importo_acquisto = 70
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 7

def test_calcola_punti_fedelta_ottanta_euro():
    # Given
    importo_acquisto = 80
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 8

def test_calcola_punti_fedelta_novanta_euro():
    # Given
    importo_acquisto = 90
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 9

def test_calcola_punti_fedelta_novantanove_euro_novantanove():
    # Given
    importo_acquisto = 99.99
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 9


# --- ACQUISTI TRA 100 E 900 EURO ---

def test_calcola_punti_fedelta_cento_euro():
    # Given
    importo_acquisto = 100
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 10

def test_calcola_punti_fedelta_cento_cinque_euro():
    # Given
    importo_acquisto = 105.50
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 10

def test_calcola_punti_fedelta_centocinquanta_euro():
    # Given
    importo_acquisto = 150
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 15

def test_calcola_punti_fedelta_duecento_euro():
    # Given
    importo_acquisto = 200
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 20

def test_calcola_punti_fedelta_duecentocinquanta_euro():
    # Given
    importo_acquisto = 250
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 25

def test_calcola_punti_fedelta_trecento_euro():
    # Given
    importo_acquisto = 300
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 30

def test_calcola_punti_fedelta_quattrocento_euro():
    # Given
    importo_acquisto = 400
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 40

def test_calcola_punti_fedelta_cinquecento_euro():
    # Given
    importo_acquisto = 500
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 50

def test_calcola_punti_fedelta_seicento_euro():
    # Given
    importo_acquisto = 600
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 60

def test_calcola_punti_fedelta_settecento_euro():
    # Given
    importo_acquisto = 700
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 70

def test_calcola_punti_fedelta_ottocento_euro():
    # Given
    importo_acquisto = 800
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 80

def test_calcola_punti_fedelta_novecento_euro():
    # Given
    importo_acquisto = 900
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 90

def test_calcola_punti_fedelta_novecentosessantanove_euro():
    # Given
    importo_acquisto = 999.99
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 99


# --- ACQUISTI DI GRANDE IMPORTO (1.000€ - 100.000€) ---

def test_calcola_punti_fedelta_mille_euro():
    # Given
    importo_acquisto = 1000
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 100

def test_calcola_punti_fedelta_millecinquecento_euro():
    # Given
    importo_acquisto = 1500
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 150

def test_calcola_punti_fedelta_duemila_euro():
    # Given
    importo_acquisto = 2000
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 200

def test_calcola_punti_fedelta_cinquemila_euro():
    # Given
    importo_acquisto = 5000
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 500

def test_calcola_punti_fedelta_diecimila_euro():
    # Given
    importo_acquisto = 10000
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 1000

def test_calcola_punti_fedelta_cinquantamila_euro():
    # Given
    importo_acquisto = 50000
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 5000

def test_calcola_punti_fedelta_centomila_euro():
    # Given
    importo_acquisto = 100000
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 10000

def test_calcola_punti_fedelta_ottantacinque_centesimi():
    # Given
    importo_acquisto = 0.85
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_quattro_euro_e_dodici():
    # Given
    importo_acquisto = 4.12
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_sei_euro_e_quarantacinque():
    # Given
    importo_acquisto = 6.45
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_otto_euro_e_trenta():
    # Given
    importo_acquisto = 8.30
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_nove_euro_e_ottantacinque():
    # Given
    importo_acquisto = 9.85
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0


# --- ACQUISTI DIVERSIFICATI TRA 10 E 50 EURO ---

def test_calcola_punti_fedelta_dieci_euro_e_cinquanta():
    # Given
    importo_acquisto = 10.50
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 1

def test_calcola_punti_fedelta_quattordici_euro_e_ottanta():
    # Given
    importo_acquisto = 14.80
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 1

def test_calcola_punti_fedelta_diciasette_euro_e_venticinque():
    # Given
    importo_acquisto = 17.25
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 1

def test_calcola_punti_fedelta_ventuno_euro_e_trenta():
    # Given
    importo_acquisto = 21.30
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 2

def test_calcola_punti_fedelta_ventiquattro_euro_e_novanta():
    # Given
    importo_acquisto = 24.90
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 2

def test_calcola_punti_fedelta_ventisette_euro_e_sessantacinque():
    # Given
    importo_acquisto = 27.65
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 2

def test_calcola_punti_fedelta_trentaquattro_euro_e_venti():
    # Given
    importo_acquisto = 34.20
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 3

def test_calcola_punti_fedelta_trentotto_euro_e_quarantacinque():
    # Given
    importo_acquisto = 38.45
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 3

def test_calcola_punti_fedelta_quarantadue_euro_e_ottantacinque():
    # Given
    importo_acquisto = 42.85
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 4

def test_calcola_punti_fedelta_quarantasei_euro_e_quindici():
    # Given
    importo_acquisto = 46.15
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 4

def test_calcola_punti_fedelta_quarantotto_euro_e_settanta():
    # Given
    importo_acquisto = 48.70
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 4


# --- ACQUISTI DIVERSIFICATI TRA 50 E 100 EURO ---

def test_calcola_punti_fedelta_cinquantatre_euro_e_quaranta():
    # Given
    importo_acquisto = 53.40
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 5

def test_calcola_punti_fedelta_cinquantanove_euro_e_settantacinque():
    # Given
    importo_acquisto = 59.75
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 5

def test_calcola_punti_fedelta_sessantuno_euro_e_venti():
    # Given
    importo_acquisto = 61.20
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 6

def test_calcola_punti_fedelta_sessantasette_euro_e_novanta():
    # Given
    importo_acquisto = 67.90
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 6

def test_calcola_punti_fedelta_settantatre_euro_e_quindici():
    # Given
    importo_acquisto = 73.15
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 7

def test_calcola_punti_fedelta_settantotto_euro_e_ottanta():
    # Given
    importo_acquisto = 78.80
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 7

def test_calcola_punti_fedelta_ottantaquattro_euro_e_cinquanta():
    # Given
    importo_acquisto = 84.50
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 8

def test_calcola_punti_fedelta_novantadue_euro_e_dieci():
    # Given
    importo_acquisto = 92.10
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 9

def test_calcola_punti_fedelta_novantasette_euro_e_quarantacinque():
    # Given
    importo_acquisto = 97.45
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 9


# --- ACQUISTI DIVERSIFICATI TRA 100 E 500 EURO ---

def test_calcola_punti_fedelta_cento_euro_e_quarantacinque():
    # Given
    importo_acquisto = 100.45
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 10

def test_calcola_punti_fedelta_centonove_euro_e_ottanta():
    # Given
    importo_acquisto = 109.80
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 10

def test_calcola_punti_fedelta_centoquindici_euro_e_trenta():
    # Given
    importo_acquisto = 115.30
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 11

def test_calcola_punti_fedelta_centoventiquattro_euro_e_sessanta():
    # Given
    importo_acquisto = 124.60
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 12

def test_calcola_punti_fedelta_centotrentotto_euro_e_novanta():
    # Given
    importo_acquisto = 138.90
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 13

def test_calcola_punti_fedelta_centoquarantasette_euro_e_venticinque():
    # Given
    importo_acquisto = 147.25
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 14

def test_calcola_punti_fedelta_centosessantotto_euro_e_quarantacinque():
    # Given
    importo_acquisto = 168.45
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 16

def test_calcola_punti_fedelta_centosettantadue_euro_e_novanta():
    # Given
    importo_acquisto = 172.90
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 17

def test_calcola_punti_fedelta_centottantanove_euro_e_cinquanta():
    # Given
    importo_acquisto = 189.50
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 18

def test_calcola_punti_fedelta_duecentocinque_euro_e_venti():
    # Given
    importo_acquisto = 205.20
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 20

def test_calcola_punti_fedelta_duecentotrentaquattro_euro_e_cinquanta():
    # Given
    importo_acquisto = 234.50
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 23

def test_calcola_punti_fedelta_duecentottantatre_euro_e_quaranta():
    # Given
    importo_acquisto = 283.40
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 28

def test_calcola_punti_fedelta_trecentotredici_euro_e_ottanta():
    # Given
    importo_acquisto = 313.80
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 31

def test_calcola_punti_fedelta_trecentosessantasei_euro_e_quindici():
    # Given
    importo_acquisto = 366.15
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 36

def test_calcola_punti_fedelta_quattrocentodiciotto_euro_e_trenta():
    # Given
    importo_acquisto = 418.30
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 41

def test_calcola_punti_fedelta_quattrocentosessantadue_euro_e_novanta():
    # Given
    importo_acquisto = 462.90
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 46

def test_calcola_punti_fedelta_cinquanta_centesimi():
    # Given
    importo_acquisto = 0.50
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_due_euro_e_quindici():
    # Given
    importo_acquisto = 2.15
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_tre_euro_e_ottanta():
    # Given
    importo_acquisto = 3.80
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_sette_euro_e_dieci():
    # Given
    importo_acquisto = 7.10
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0

def test_calcola_punti_fedelta_nove_euro_e_novanta():
    # Given
    importo_acquisto = 9.90
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 0


# --- ACQUISTI TRA 10 E 20 EURO ---

def test_calcola_punti_fedelta_esattamente_dieci_euro_tondi():
    # Given
    importo_acquisto = 10.00
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 1

def test_calcola_punti_fedelta_dodici_euro_e_quaranta():
    # Given
    importo_acquisto = 12.40
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 1

def test_calcola_punti_fedelta_quindici_euro_e_novantanove():
    # Given
    importo_acquisto = 15.99
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 1

def test_calcola_punti_fedelta_diciotto_euro_e_venti():
    # Given
    importo_acquisto = 18.20
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 1

def test_calcola_punti_fedelta_diciannove_euro_e_novantacinque():
    # Given
    importo_acquisto = 19.95
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 1


# --- ACQUISTI TRA 20 E 50 EURO ---

def test_calcola_punti_fedelta_ventidue_euro_e_trenta():
    # Given
    importo_acquisto = 22.30
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 2

def test_calcola_punti_fedelta_ventisei_euro_e_ottanta():
    # Given
    importo_acquisto = 26.80
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 2

def test_calcola_punti_fedelta_ventinove_euro_e_cinquanta():
    # Given
    importo_acquisto = 29.50
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 2

def test_calcola_punti_fedelta_trentuno_euro_e_venti():
    # Given
    importo_acquisto = 31.20
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 3

def test_calcola_punti_fedelta_trentacinque_euro_e_settanta():
    # Given
    importo_acquisto = 35.70
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 3

def test_calcola_punti_fedelta_trentanove_euro_e_dieci():
    # Given
    importo_acquisto = 39.10
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 3

def test_calcola_punti_fedelta_quarantatre_euro_e_quaranta():
    # Given
    importo_acquisto = 43.40
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 4

def test_calcola_punti_fedelta_quarantasette_euro_e_novanta():
    # Given
    importo_acquisto = 47.90
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 4


# --- ACQUISTI TRA 50 E 100 EURO ---

def test_calcola_punti_fedelta_cinquantuno_euro_e_venti():
    # Given
    importo_acquisto = 51.20
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 5

def test_calcola_punti_fedelta_cinquantasei_euro_e_ottanta():
    # Given
    importo_acquisto = 56.80
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 5

def test_calcola_punti_fedelta_sessantadue_euro_e_quindici():
    # Given
    importo_acquisto = 62.15
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 6

def test_calcola_punti_fedelta_sessantasette_euro_e_quaranta():
    # Given
    importo_acquisto = 67.40
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 6

def test_calcola_punti_fedelta_settantuno_euro_e_novanta():
    # Given
    importo_acquisto = 71.90
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 7

def test_calcola_punti_fedelta_settantotto_euro_e_trenta():
    # Given
    importo_acquisto = 78.30
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 7

def test_calcola_punti_fedelta_ottantadue_euro_e_sessanta():
    # Given
    importo_acquisto = 82.60
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 8

def test_calcola_punti_fedelta_ottantasette_euro_e_dieci():
    # Given
    importo_acquisto = 87.10
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 8

def test_calcola_punti_fedelta_novantatre_euro_e_quarantacinque():
    # Given
    importo_acquisto = 93.45
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 9

def test_calcola_punti_fedelta_novantotto_euro_e_novanta():
    # Given
    importo_acquisto = 98.90
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 9


# --- ACQUISTI DIVERSIFICATI TRA 100 E 600 EURO ---

def test_calcola_punti_fedelta_centodue_euro_e_trenta():
    # Given
    importo_acquisto = 102.30
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 10

def test_calcola_punti_fedelta_centoquattordici_euro_e_venti():
    # Given
    importo_acquisto = 114.20
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 11

def test_calcola_punti_fedelta_centoventisette_euro_e_ottanta():
    # Given
    importo_acquisto = 127.80
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 12

def test_calcola_punti_fedelta_centotrentatre_euro_e_cinquanta():
    # Given
    importo_acquisto = 133.50
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 13

def test_calcola_punti_fedelta_centoquarantanove_euro_e_novanta():
    # Given
    importo_acquisto = 149.90
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 14

def test_calcola_punti_fedelta_centosessantotto_euro_e_dieci():
    # Given
    importo_acquisto = 158.10
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 15

def test_calcola_punti_fedelta_centosessantaquattro_euro_e_settanta():
    # Given
    importo_acquisto = 164.70
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 16

def test_calcola_punti_fedelta_centosettantanove_euro_e_trenta():
    # Given
    importo_acquisto = 179.30
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 17

def test_calcola_punti_fedelta_centottantacinque_euro():
    # Given
    importo_acquisto = 185.00
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 18

def test_calcola_punti_fedelta_centonovantadue_euro_e_quaranta():
    # Given
    importo_acquisto = 192.40
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 19

def test_calcola_punti_fedelta_duecentocindici_euro_e_sessanta():
    # Given
    importo_acquisto = 215.60
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 21

def test_calcola_punti_fedelta_duecentotrentotto_euro_e_novanta():
    # Given
    importo_acquisto = 238.90
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 23

def test_calcola_punti_fedelta_duecentosessantasette_euro_e_trenta():
    # Given
    importo_acquisto = 267.30
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 26

def test_calcola_punti_fedelta_duecentonovantaquattro_euro_e_dieci():
    # Given
    importo_acquisto = 294.10
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 29

def test_calcola_punti_fedelta_trecentoventuno_euro_e_cinquanta():
    # Given
    importo_acquisto = 321.50
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 32

def test_calcola_punti_fedelta_trecentocinquantanove_euro_e_ottanta():
    # Given
    importo_acquisto = 359.80
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 35

def test_calcola_punti_fedelta_trecentottantaquattro_euro_e_venti():
    # Given
    importo_acquisto = 384.20
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 38

def test_calcola_punti_fedelta_quattrocentododici_euro_e_novanta():
    # Given
    importo_acquisto = 412.90
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 41

def test_calcola_punti_fedelta_quattrocentocinquantacinque_euro():
    # Given
    importo_acquisto = 455.00
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 45

def test_calcola_punti_fedelta_quattrocentottantanove_euro_e_trenta():
    # Given
    importo_acquisto = 489.30
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 48

def test_calcola_punti_fedelta_cinquecentoventitre_euro_e_settanta():
    # Given
    importo_acquisto = 523.70
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 52

def test_calcola_punti_fedelta_cinquecentosettantotto_euro_e_quaranta():
    # Given
    importo_acquisto = 578.40
    # When
    punti_ottenuti = calcola_punti_fedelta(importo_acquisto)
    # Then
    assert punti_ottenuti == 57