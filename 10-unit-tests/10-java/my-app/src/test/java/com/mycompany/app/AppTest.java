package com.mycompany.app;

import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

public class AppTest {
    public App app = new App();
    @Test
    public void mainTestHelloWorld() {
        app.main(new String[]{});
    }
}
