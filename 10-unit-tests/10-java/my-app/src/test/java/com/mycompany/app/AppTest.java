package com.mycompany.app;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

/**
 * Unit test for simple App.
 */
public class AppTest {

    /**
     * Rigorous Test :-)
     */
    @Test
    public void shouldAnswerWithTrue() {
        assertTrue(true);
    }

    @Test
    public void testSomma() {
        int risultato = App.somma(10, 5);
        assertEquals(15, risultato);
    }

    @Test
    public void testMoltiplica() {
        int risultato = App.moltiplica(10, 5);
        assertEquals(50, risultato);
    }

    @Test
    public void testVerificaPari() {
        App.verificaPari(6);
        
       
        App.verificaPari(7);
    }

    @Test
    public void testMain() {
        App.main(new String[]{});
    }

}
