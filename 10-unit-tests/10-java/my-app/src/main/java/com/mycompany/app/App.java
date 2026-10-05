package com.mycompany.app;

import java.util.Scanner;

public class App {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean continua = true;

        System.out.println("=================================");
        System.out.println("   BENVENUTO IN CALCOLATRICE    ");
        System.out.println("=================================");

        while (continua) {
            mostraMenu();
            System.out.print("Scegli un'operazione (1-5): ");

            if (!scanner.hasNextInt()) {
                System.out.println("Errore: Inserisci un numero valido per la scelta.");
                scanner.next();
                continue;
            }

            int scelta = scanner.nextInt();

            if (scelta == 5) {
                continua = false;
                System.out.println("\nGrazie per aver usato la calcolatrice. Arrivederci!");
                break;
            }

            if (scelta < 1 || scelta > 5) {
                System.out.println("Scelta non valida. Riprova.");
                continue;
            }

            System.out.print("Inserisci il primo numero: ");
            double num1 = leggiNumero(scanner);

            System.out.print("Inserisci il secondo numero: ");
            double num2 = leggiNumero(scanner);

            eseguiOperazione(scelta, num1, num2);

            System.out.println("---------------------------------");
        }

        scanner.close();
    }

    private static void mostraMenu() {
        System.out.println("\nSeleziona l'operazione desiderata:");
        System.out.println("1. Addizione (+)");
        System.out.println("2. Sottrazione (-)");
        System.out.println("3. Moltiplicazione (*)");
        System.out.println("4. Divisione (/)");
        System.out.println("5. Esci");
    }

    private static double leggiNumero(Scanner scanner) {
        while (!scanner.hasNextDouble()) {
            System.out.println("Errore: Inserisci un numero intero o decimale valido.");
            System.out.print("Riprova: ");
            scanner.next();
        }
        return scanner.nextDouble();
    }

    // --- Metodi per le operazioni matematiche ---

    public static double addizione(double a, double b) {
        return a + b;
    }

    public static double sottrazione(double a, double b) {
        return a - b;
    }

    public static double moltiplicazione(double a, double b) {
        return a * b;
    }

    public static double divisione(double a, double b) {
        if (b == 0) {
            System.out.println("\nErrore: Impossibile dividere per zero!");
            return Double.NaN;
        }
        return a / b;
    }

    // --- Metodo gestore dell'esecuzione ---

    private static void eseguiOperazione(int scelta, double a, double b) {
        double risultato = 0;

        switch (scelta) {
            case 1:
                risultato = addizione(a, b);
                System.out.printf("\nRisultato: %.2f + %.2f = %.2f\n", a, b, risultato);
                break;
            case 2:
                risultato = sottrazione(a, b);
                System.out.printf("\nRisultato: %.2f - %.2f = %.2f\n", a, b, risultato);
                break;
            case 3:
                risultato = moltiplicazione(a, b);
                System.out.printf("\nRisultato: %.2f * %.2f = %.2f\n", a, b, risultato);
                break;
            case 4:
                risultato = divisione(a, b);
                if (!Double.isNaN(risultato)) {
                    System.out.printf("\nRisultato: %.2f / %.2f = %.2f\n", a, b, risultato);
                }
                break;
        }
    }
}