package com.mycompany.app;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class PersonaTest {

    @Test
    public void testCostruttoreEGetters() {
        Persona persona = new Persona("Mario", "Rossi");
        
        assertEquals("Mario", persona.getNome());
        assertEquals("Rossi", persona.getCognome());
    }

    @Test
    public void testSetters() {
        Persona persona = new Persona("Mario", "Rossi");
        
        persona.setNome("Luigi");
        persona.setCognome("Verdi");

        assertEquals("Luigi", persona.getNome());
        assertEquals("Verdi", persona.getCognome());
    }

    @Test
    public void testToString() {
        Persona persona = new Persona("Mario", "Rossi");
        String stringaAttesa = "Persona [nome=Mario, cognome=Rossi]";
        
        assertEquals(stringaAttesa, persona.toString());
    }
}