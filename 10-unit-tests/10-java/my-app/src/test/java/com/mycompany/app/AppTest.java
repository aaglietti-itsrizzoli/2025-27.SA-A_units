package com.mycompany.app;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import org.junit.jupiter.api.Test;

class AppTest {

    @Test
    void scriveQuandoC_eInchiostroSufficiente() {
        Pennarello pennarello = new Pennarello();
        Inchiostro inchiostro = new Inchiostro();
        inchiostro.setQuantita(10);
        ByteArrayOutputStream output = new ByteArrayOutputStream();
        PrintStream outputOriginale = System.out;

        try {
            System.setOut(new PrintStream(output));
            pennarello.scrivi("ciao", inchiostro);
        } finally {
            System.setOut(outputOriginale);
        }

        assertEquals(2, inchiostro.getQuantita());
        assertEquals("Hai scritto: ciao" + System.lineSeparator(), output.toString());
    }

    @Test
    void nonScriveQuandoL_inchiostroE_insufficiente() {
        Pennarello pennarello = new Pennarello();
        Inchiostro inchiostro = new Inchiostro();
        inchiostro.setQuantita(7);
        ByteArrayOutputStream output = new ByteArrayOutputStream();
        PrintStream outputOriginale = System.out;

        try {
            System.setOut(new PrintStream(output));
            pennarello.scrivi("ciao", inchiostro);
        } finally {
            System.setOut(outputOriginale);
        }

        assertEquals(7, inchiostro.getQuantita());
        assertEquals("Non hai abbastanza inchiostro per scrivere." + System.lineSeparator(), output.toString());
    }

    @Test
    void mainStampaIlSaluto() {
        new App();
        ByteArrayOutputStream output = new ByteArrayOutputStream();
        PrintStream outputOriginale = System.out;

        try {
            System.setOut(new PrintStream(output));
            App.main(new String[0]);
        } finally {
            System.setOut(outputOriginale);
        }

        assertEquals("Hello World!" + System.lineSeparator(), output.toString());
    }
}
