package com.mycompany.app;

public class Pennarello {
    public void scrivi(String testo, Inchiostro inchiostro) {
        int caratteri = testo.length();
        int consumo = caratteri * 2;

        if (inchiostro.getQuantita() >= consumo) {
            inchiostro.setQuantita(inchiostro.getQuantita() - consumo);
            System.out.println("Hai scritto: " + testo);
        } else {
            System.out.println("Non hai abbastanza inchiostro per scrivere.");
        }
    }
}
