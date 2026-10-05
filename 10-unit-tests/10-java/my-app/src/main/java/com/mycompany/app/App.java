package com.mycompany.app;

import java.util.Scanner;

public class App {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Dimmi un numero e verifico se è palindromo:");
        
        if (sc.hasNextInt()) {
            int numero = sc.nextInt();
            if (isPalindrome(numero)) {
                System.out.println("Il numero è palindromo");
            } else {
                System.out.println("Il numero non è palindromo");
            }
        } else {
            System.out.println("Input non valido");
        }
    }

    public static boolean isPalindrome(int numero) {
        if (numero < 0) {
            return false;
        }

        int ogNumero = numero;
        int inverso = 0;

        while (numero != 0) {
            int cifra = numero % 10;
            inverso = inverso * 10 + cifra;
            numero = numero / 10;
        }

        return inverso == ogNumero;
    }
}