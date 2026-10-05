# i tuoi test di unità qua
import pytest
import ecommerce


def test_calcola_punti_fedelta_zero_punti_per_dieci_euro_acquisto():
    punti_fedelta = ecommerce.calcola_punti_fedelta(3,2)
    assert punti_fedelta == 3


# Promuovi livello cliente
def test_promuovi_cliente():
    # Given: un cliente con 99 punti fedelta
    punti_iniziali = 99
    importo_acquisto = 12

    # When: un cliente conclude un acquisto di 12 euro fn:promuovi_livello_cliente
    nuovo_livello = ecommerce.promuovi_livello_cliente(punti_iniziali, importo_acquisto)

    # Then: il cliente viene promosso al livello silver
    assert nuovo_livello == "silver"


# Costo spedizione
def test_consegna_espressa():
    # Given: una spedizione di 27 kg, a 67 km, espressa
    peso_kg = 27
    distanza_km = 67
    consegna_espressa = True

    # When: un cliente inserisce l'indirizzo di consegna e seleziona consegna espressa
    costo_totale = ecommerce.calcola_costo_spedizione(
        peso=peso_kg, 
        distanza=distanza_km, 
        espressa=True,
    )

    # Then: la consegna costa 17.84
    assert costo_totale == 17.84

