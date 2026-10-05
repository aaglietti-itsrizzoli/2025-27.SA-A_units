package com.mycompany.app;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class LavoratoreTest {

    @Test
    public void testCostruttoreDueParametri() {
        Lavoratore lavoratore = new Lavoratore("Mario", "Rossi");

        assertEquals("Mario", lavoratore.getNome());
        assertEquals("Rossi", lavoratore.getCognome());
        assertEquals(0.0, lavoratore.getSalario(), 0.001);
    }

    @Test
    public void testCostruttoreTreParametriEGettersSetters() {
        Lavoratore lavoratore = new Lavoratore("Mario", "Rossi", 1500.0);

        assertEquals("Mario", lavoratore.getNome());
        assertEquals("Rossi", lavoratore.getCognome());
        assertEquals(1500.0, lavoratore.getSalario(), 0.001);

        lavoratore.setSalario(1800.50);
        assertEquals(1800.50, lavoratore.getSalario(), 0.001);
    }

    @Test
    public void testPresentati() {
        Lavoratore lavoratore = new Lavoratore("Mario", "Rossi", 1500.0);
        assertDoesNotThrow(() -> lavoratore.Presentati());
    }

    @Test
    public void testToString() {
        Lavoratore lavoratore = new Lavoratore("Mario", "Rossi", 1500.0);
        String stringaAttesa = "Lavoratore [salario=1500.0Persona [nome=Mario, cognome=Rossi]]";

        assertEquals(stringaAttesa, lavoratore.toString());
    }
}