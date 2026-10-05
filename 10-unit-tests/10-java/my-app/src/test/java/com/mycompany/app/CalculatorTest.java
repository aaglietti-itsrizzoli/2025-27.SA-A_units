package com.mycompany.app;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class CalculatorTest {

    @Test
    public void testAdd() {

        Calculator calculator = new Calculator();

        assertEquals(5, calculator.add(2, 3));
        assertEquals(15, calculator.add(10, 5));
        assertEquals(0, calculator.add(-2, 2));
        assertEquals(-7, calculator.add(-3, -4));
    }

    @Test
    public void testIsEven() {

        Calculator calculator = new Calculator();

        assertTrue(calculator.isEven(2));
        assertTrue(calculator.isEven(4));
        assertTrue(calculator.isEven(0));

        assertFalse(calculator.isEven(3));
        assertFalse(calculator.isEven(7));
        assertFalse(calculator.isEven(-5));
    }
}