package com.mycompany.app;

import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.assertEquals;
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
    public void testMain() {

        App app = new App();
        // Cattura l'output del metodo main
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        PrintStream printStream = new PrintStream(outputStream);
        System.setOut(printStream);

        // Chiama il metodo main
        App.main(new String[]{});

        // Verifica l'output
        String expectedOutput = "Hello World!" + System.lineSeparator();
        assertEquals(expectedOutput, outputStream.toString());
        

    }
}
