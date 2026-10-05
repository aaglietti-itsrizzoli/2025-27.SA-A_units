package com.mycompany.app;

/**
 * Hello world!
 */
public class App {
  public static void main(String[] args) {
        int x = 10;
        int y = 5;

        // 1. Calcolo semplice (somma)
        int risultatoSomma = somma(x, y);
        System.out.println("La somma tra " + x + " e " + y + " è: " + risultatoSomma);

        // 2. Calcolo semplice (moltiplicazione)
        int risultatoProdotto = moltiplica(x, y);
        System.out.println("Il prodotto tra " + x + " e " + y + " è: " + risultatoProdotto);

        // 3. Verifica ed esito (numero pari o dispari)
        verificaPari(x);
        verificaPari(7);
    }

    // Metodo per sommare due numeri
    public static int somma(int a, int b) {
        return a + b;
    }

    // Metodo per moltiplicare due numeri
    public static int moltiplica(int a, int b) {
        return a * b;
    }

    // Metodo per verificare se un numero è pari o dispari e stampare il risultato
    public static void verificaPari(int numero) {
        if (numero % 2 == 0) {
            System.out.println("Il numero " + numero + " è PARI.");
        } else {
            System.out.println("Il numero " + numero + " è DISPARI.");
        }
    }


}
