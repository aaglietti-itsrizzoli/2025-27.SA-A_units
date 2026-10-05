package com.mycompany.app;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

public class CalculatorTest {

    @Test
    @DisplayName("Given due interi, When sommati, Then restituisce la somma corretta")
    public void testAdd() {
  
        Calculator calc = new Calculator();
        int a = 10;
        int b = 5;

   
        int result = calc.add(a, b);

    
        assertEquals(15, result);
    }

    @Test
    @DisplayName("Given due interi validi, When divisi, Then restituisce il quoziente")
    public void testDivideSuccess() {

        Calculator calc = new Calculator();
        int a = 10;
        int b = 2;

        int result = calc.divide(a, b);

        assertEquals(5, result);
    }

    @Test
    @DisplayName("Given divisore pari a zero, When diviso, Then lancia IllegalArgumentException")
    public void testDivideByZero() {

        Calculator calc = new Calculator();


        assertThrows(IllegalArgumentException.class, () -> {
            calc.divide(10, 0);
        });
    }
}