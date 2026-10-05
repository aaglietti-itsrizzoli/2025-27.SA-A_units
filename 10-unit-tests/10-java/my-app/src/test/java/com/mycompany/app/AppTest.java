package com.mycompany.app;

import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class AppTest {

    @Test
    public void shouldAnswerWithTrue() {
        assertTrue(true);
    }

    @Test
    public void testMain() {
        App.main(new String[]{});
    }

    @Test
    public void testAppConstructor() {
        App app = new App();
        assertNotNull(app);
    }
}