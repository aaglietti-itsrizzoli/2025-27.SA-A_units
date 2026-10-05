package com.mycompany.app;

import static org.junit.jupiter.api.Assertions.*;

import java.io.ByteArrayInputStream;
import java.io.InputStream;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

public class AppTest {

    // 1. Copre il costruttore predefinito della classe App
    @Test
    @DisplayName("Test costruttore App")
    public void testCostruttoreApp() {
        App app = new App();
        assertNotNull(app);
    }

    // 2. Copre i vari rami del metodo statico isPalindrome
    @Test
    @DisplayName("Test numero palindromo positivo")
    public void testIsPalindromePositivo() {
        assertTrue(App.isPalindrome(121));
        assertTrue(App.isPalindrome(0));
    }

    @Test
    @DisplayName("Test numero non palindromo positivo")
    public void testIsPalindromeNonPalindromo() {
        assertFalse(App.isPalindrome(123));
    }

    @Test
    @DisplayName("Test numero negativo")
    public void testIsPalindromeNegativo() {
        assertFalse(App.isPalindrome(-121));
    }

    // 3. Copre tutti i rami e le righe del metodo main simulando l'input dello Scanner
    @Test
    @DisplayName("Test main con numero palindromo")
    public void testMainConNumeroPalindromo() {
        String input = "121\n";
        InputStream sysInBackup = System.in;
        try {
            System.setIn(new ByteArrayInputStream(input.getBytes()));
            App.main(new String[]{});
        } finally {
            System.setIn(sysInBackup);
        }
    }

    @Test
    @DisplayName("Test main con numero non palindromo")
    public void testMainConNumeroNonPalindromo() {
        String input = "123\n";
        InputStream sysInBackup = System.in;
        try {
            System.setIn(new ByteArrayInputStream(input.getBytes()));
            App.main(new String[]{});
        } finally {
            System.setIn(sysInBackup);
        }
    }

    @Test
    @DisplayName("Test main con input non numerico")
    public void testMainConInputNonValido() {
        String input = "abc\n";
        InputStream sysInBackup = System.in;
        try {
            System.setIn(new ByteArrayInputStream(input.getBytes()));
            App.main(new String[]{});
        } finally {
            System.setIn(sysInBackup);
        }
    }
}