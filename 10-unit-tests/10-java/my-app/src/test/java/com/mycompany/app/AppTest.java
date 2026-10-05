package com.mycompany.app;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertNotNull;

public class AppTest {
    
    @Test
    public void testAppConstructor() {
        App app = new App();
        assertNotNull(app);
    }

    @Test
    public void testMain() {
        String[] args = {};
        App.main(args);
    }
}