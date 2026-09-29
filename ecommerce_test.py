import pytest
import ecommerce
import sys

# 0 Punti fedeltà
def test_calcola_punti_fedelta_zero_punti_per_dieci_euro_acquisto():
    # Given un acquisto di 3 euro
    importo_acquisto = 3
    
    # When un cliente conclude un acquisto fn:calcola_punti_fedelta ne calcola i punti fedeltà
    punti_fedelta = ecommerce.calcola_punti_fedelta(importo_acquisto)
    
    # Then il cliente riceve 0 punti fedeltà perchè l'acquisto è inferiore a 10 euro
    assert punti_fedelta == 0


# 1 Prezzo scontato
def test_calcola_prezzo_scontato_prezzo_negativo_percentuale_sconto_non_intera():
    # Given un prezzo negativo (-4 euro) and una percentuale di sconto non intera (0.75)
    prezzo = -4
    sconto = 0.75
    
    # When fn:calcola_prezzo_scontato calcola il nuovo prezzo
    # Then la funzione dovrebbe raise ValueError per input non validi
    with pytest.raises(ValueError):
        ecommerce.calcola_prezzo_scontato(prezzo, sconto)


# 2 Articoli esauriti
def test_svuota_articoli_esauriti_articolo_non_esistente():
    # Given un prodotto che non esiste nel magazzino
    righe_carrello = [{"nome": "prodotto_A"}, {"nome": "prodotto_B"}]
    # Il magazzino contiene solo prodotto_A; prodotto_B o altri prodotti inesistenti non ci sono
    magazzino = {"prodotto_A": 5}
    
    # When la funzione fn:svuota_articoli_esauriti viene chiamata
    nuova_lista = ecommerce.svuota_articoli_esauriti(righe_carrello, magazzino)
    
    # Then la funzione ritorna una nuova lista
    assert isinstance(nuova_lista, list)
    assert nuova_lista is not righe_carrello
    # Ritorna solo le righe disponibili in magazzino (>0)
    assert nuova_lista == [{"nome": "prodotto_A"}]

    # 3 Livello cliente
def test_promuovi_livello_cliente_punti_valore_altissimo():
    # Given un numero di punti oltre il limite integer
    punti_oltre_limite = sys.maxsize + 1  # es. 9223372036854775808
    
    # When la funzione fn:promuovi_livello_cliente viene chiamata con questo valore
    # Then la funzione va in errore (es. ValueError o OverflowError)
    with pytest.raises((ValueError, OverflowError)):
        ecommerce.promuovi_livello_cliente(punti_oltre_limite)