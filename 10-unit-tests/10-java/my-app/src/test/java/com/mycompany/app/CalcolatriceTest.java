package com.mycompany.app;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class CalcolatriceTest {

    @Test
    public void testSommaDiDueNumeri() {
        Calcolatrice calc = new Calcolatrice();
        int risultato = calc.somma(5, 3);
        assertEquals(8, risultato);
    }
}