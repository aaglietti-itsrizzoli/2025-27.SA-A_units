package com.mycompany.app;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class AppTest {

    @Test
    @DisplayName("Test Addizione con numeri positivi")
    void testAddizionePositivi() {
        double risultato = App.addizione(5.0, 3.0);
        assertEquals(8.0, risultato, 0.0001, "5 + 3 dovrebbe essere 8");
    }

    @Test
    @DisplayName("Test Addizione con numeri negativi")
    void testAddizioneNegativi() {
        double risultato = App.addizione(-4.0, -2.0);
        assertEquals(-6.0, risultato, 0.0001, "-4 + (-2) dovrebbe essere -6");
    }

    @Test
    @DisplayName("Test Sottrazione")
    void testSottrazione() {
        double risultato = App.sottrazione(10.0, 4.0);
        assertEquals(6.0, risultato, 0.0001, "10 - 4 dovrebbe essere 6");
    }

    @Test
    @DisplayName("Test Moltiplicazione")
    void testMoltiplicazione() {
        double risultato = App.moltiplicazione(3.0, 4.0);
        assertEquals(12.0, risultato, 0.0001, "3 * 4 dovrebbe essere 12");
    }

    @Test
    @DisplayName("Test Moltiplicazione per zero")
    void testMoltiplicazionePerZero() {
        double risultato = App.moltiplicazione(7.5, 0.0);
        assertEquals(0.0, risultato, 0.0001, "Moltiplicazione per zero deve dare 0");
    }

    @Test
    @DisplayName("Test Divisione valida")
    void testDivisioneValida() {
        double risultato = App.divisione(10.0, 2.0);
        assertEquals(5.0, risultato, 0.0001, "10 / 2 dovrebbe essere 5");
    }

    @Test
    @DisplayName("Test Divisione per zero (ritorna Double.NaN)")
    void testDivisionePerZero() {
        double risultato = App.divisione(10.0, 0.0);
        assertTrue(Double.isNaN(risultato), "La divisione per zero deve restituire Double.NaN");
    }
}