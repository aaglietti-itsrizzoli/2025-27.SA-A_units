package com.mycompany.app;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class AppTest {

    private App app;

    @BeforeEach
    public void setUp() {
        app = new App();
    }

    @Test
    public void testLibroGettersAndSetters() {
        App.Libro libro = new App.Libro("Titolo", "Autore", 1999, 100.0);
        
        assertEquals("Titolo", libro.getTitolo());
        assertEquals("Autore", libro.getAutore());
        assertEquals(1999, libro.getAnnoPubblicazione());
        assertEquals(100.0, libro.getPrezzo());

        libro.setPrezzo(80.0);
        assertEquals(80.0, libro.getPrezzo());
    }

    @Test
    public void testLibroToString() {
        App.Libro libro = new App.Libro("1984", "Orwell", 1949, 15.0);
        String risultato = libro.toString();
        assertTrue(risultato.contains("1984"));
        assertTrue(risultato.contains("Orwell"));
    }

    @Test
    public void testAddLibroEGetters() {
        App.Libro l1 = new App.Libro("1984", "George Orwell", 1949, 15.00);
        app.addLibro(l1);

        assertEquals(1, app.getCatalogo().size());
        assertEquals(1, app.getArrayLibri().length);
        assertEquals("1984", app.getArrayLibri()[0].getTitolo());

        // Test il ramo del null (branch coverage)
        app.addLibro(null);
        assertEquals(1, app.getCatalogo().size());
    }

    @Test
    public void testApplicaScontoSeAmmesso() {
        // Ramo OK: prezzo > 50 e anno < 2000
        App.Libro libroIdoneo = new App.Libro("Libro V", "Autore", 1990, 100.0);
        assertTrue(libroIdoneo.applicaScontoSeAmmesso(20.0));
        assertEquals(80.0, libroIdoneo.getPrezzo(), 0.01);

        App.Libro libroEconomico = new App.Libro("Libro E", "Autore", 1990, 40.0);
        assertFalse(libroEconomico.applicaScontoSeAmmesso(20.0));
        assertEquals(40.0, libroEconomico.getPrezzo(), 0.01);

        App.Libro libroNuovo = new App.Libro("Libro N", "Autore", 2005, 100.0);
        assertFalse(libroNuovo.applicaScontoSeAmmesso(20.0));
        assertEquals(100.0, libroNuovo.getPrezzo(), 0.01);
    }

    @Test
    public void testApplicaScontoAiLibriIdonei() {
        App.Libro l1 = new App.Libro("Vecchio e Caro", "Autore A", 1980, 100.0); // idoneo
        App.Libro l2 = new App.Libro("Nuovo e Caro", "Autore B", 2010, 100.0);   // non idoneo
        
        app.addLibro(l1);
        app.addLibro(l2);

        app.applicaScontoAiLibriIdonei(50.0); // Sconto 50%

        assertEquals(50.0, l1.getPrezzo(), 0.01);
        assertEquals(100.0, l2.getPrezzo(), 0.01);
    }

    @Test
    public void testFiltriStream() {
        App.Libro l1 = new App.Libro("Libro 1", "Autore A", 1990, 30.0);
        App.Libro l2 = new App.Libro("Libro 2", "Autore B", 2005, 80.0);

        app.addLibro(l1);
        app.addLibro(l2);

        List<App.Libro> vecchi = app.filtraLibriPrimaDel2000();
        assertEquals(1, vecchi.size());
        assertEquals("Libro 1", vecchi.get(0).getTitolo());

        List<App.Libro> cari = app.filtraPerPrezzoMaggioreDi(50.0);
        assertEquals(1, cari.size());
        assertEquals("Libro 2", cari.get(0).getTitolo());
    }

    @Test
    public void testMain() {
        assertDoesNotThrow(() -> App.main(new String[]{}));
    }
}