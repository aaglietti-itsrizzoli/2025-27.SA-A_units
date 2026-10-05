import org.junit.jupiter.api.Test;
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;

public class AppTest {

    @Test
    void testProdotto() {
        assertEquals(30, App.prodotto(new int[]{2, 3, 5}));
        assertEquals(0, App.prodotto(new int[]{}));
        assertEquals(0, App.prodotto(null));
    }

    @Test
    void testMedia() {
        assertEquals(3.3333333f, App.media(new int[]{2, 3, 5}), 0.0001f);
        assertEquals(0.0f, App.media(new int[]{}));
        assertEquals(0.0f, App.media(null));
    }

    @Test
    void testPariDispari() {
        assertEquals(0, App.pari_dispari(4));  // Dovrebbe essere pari
        assertEquals(1, App.pari_dispari(7));  // questo dispari
        assertEquals(0, App.pari_dispari(0));  // Zero è pari
    }

    @Test
    void testVocali() {
        assertEquals(11, App.vocali("I topi non avevano nipoti"));
        assertEquals(5, App.vocali("Ciao Mondo"));
        assertEquals(0, App.vocali("bcd"));
        assertEquals(0, App.vocali(null));
    }

    @Test
    void testPalindroma() {
        assertTrue(App.palindroma("I topi non avevano nipoti"));
        assertTrue(App.palindroma("Radar"));
        assertFalse(App.palindroma("Ciao Mondo"));
        assertFalse(App.palindroma(null));
    }

    @Test
    void testFibonacci() {
        List<Integer> atteso = List.of(0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89);
        List<Integer> atteso_minz = List.of();
        assertEquals(atteso, App.fibonacci(100));
        assertEquals(atteso_minz, App.fibonacci(-1));
    }
}