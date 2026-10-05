package com.mycompany.app;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class CalculatorTest {

    private Calculator calculator;

    @BeforeEach
    public void setUp() {
        // Given the calculator is initialized
        calculator = new Calculator();
    }

    @Test
    public void testAdd() {
        // When I add 5 and 3
        int result = calculator.add(5, 3);
        // Then the result should be 8
        assertEquals(8, result);
    }

    @Test
    public void testDivideValid() {
        // When I divide 10 by 2
        int result = calculator.divide(10, 2);
        // Then the result should be 5
        assertEquals(5, result);
    }

    @Test
    public void testDivideByZero() {
        // When I divide 10 by 0
        // Then an IllegalArgumentException should be thrown
        assertThrows(IllegalArgumentException.class, () -> {
            calculator.divide(10, 0);
        });
    }
}