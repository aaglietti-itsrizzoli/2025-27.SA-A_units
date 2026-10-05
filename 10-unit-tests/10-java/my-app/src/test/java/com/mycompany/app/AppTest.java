package com.mycompany.app;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

/**
 * Unit test for simple App.
 */
public class AppTest {

    @Test 
    public void testApp(){
        App app = new App();
        assertNotNull(app);  
    }

    @Test 
    public void TestMain(){
        App.main(new String[]{});

    }
    /**
     * Rigorous Test :-)
     */
    @Test
    public void secondoMetodo() {
        String stringa = App.secondoMetodo();
        assertEquals("Ciao secondo metodo", stringa);
    }
}
