package com.mycompany.app;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class App {

    public static class Libro {
        private String titolo;
        private String autore;
        private int annoPubblicazione;
        private double prezzo;

        public Libro(String titolo, String autore, int annoPubblicazione, double prezzo) {
            this.titolo = titolo;
            this.autore = autore;
            this.annoPubblicazione = annoPubblicazione;
            this.prezzo = prezzo;
        }

        public String getTitolo() { return titolo; }
        public String getAutore() { return autore; }
        public int getAnnoPubblicazione() { return annoPubblicazione; }
        public double getPrezzo() { return prezzo; }
        public void setPrezzo(double prezzo) { this.prezzo = prezzo; }

 
        public boolean applicaScontoSeAmmesso(double percentualeSconto) {
            if (this.prezzo > 50.0 && this.annoPubblicazione < 2000) {
                this.prezzo -= this.prezzo * (percentualeSconto / 100.0);
                return true;
            }
            return false;
        }

        @Override
        public String toString() {
            return String.format("Libro{titolo='%s', autore='%s', anno=%d, prezzo=%.2f€}", 
                                 titolo, autore, annoPubblicazione, prezzo);
        }
    }

    private List<Libro> catalogo = new ArrayList<>();

    public void addLibro(Libro libro) {
        if (libro != null) {
            catalogo.add(libro);
        }
    }

    public Libro[] getArrayLibri() {
        return catalogo.toArray(new Libro[0]);
    }

    public List<Libro> getCatalogo() {
        return catalogo;
    }

    public void applicaScontoAiLibriIdonei(double percentualeSconto) {
        catalogo.forEach(libro -> libro.applicaScontoSeAmmesso(percentualeSconto));
    }


    public List<Libro> filtraLibriPrimaDel2000() {
        return catalogo.stream()
                .filter(l -> l.getAnnoPubblicazione() < 2000)
                .collect(Collectors.toList());
    }

    public List<Libro> filtraPerPrezzoMaggioreDi(double prezzoSoglia) {
        return catalogo.stream()
                .filter(l -> l.getPrezzo() > prezzoSoglia)
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        App app = new App();

        app.addLibro(new Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 60.00));
        app.addLibro(new Libro("1984", "George Orwell", 1949, 15.50));
        app.addLibro(new Libro("Harry Potter", "J.K. Rowling", 2000, 55.00));

        System.out.println("--- CATALOGO COMPLETO ---");
        for (Libro l : app.getArrayLibri()) {
            System.out.println(l);
        }

        System.out.println("\n--- APPLICAZIONE SCONTO 20% ---");
        app.applicaScontoAiLibriIdonei(20.0);
        for (Libro l : app.getArrayLibri()) {
            System.out.println(l);
        }
    }
}