import java.util.ArrayList;
import java.util.List;

public class App {

    public static void main(String[] args) {
        int[] lista = {2, 3, 5};

        System.out.println("Il prodotto è: " + prodotto(lista));
        System.out.println("La media è: " + media(lista));
        System.out.println("Numero di vocali: " + vocali("Ciao Mondo"));
        System.out.println("È palindroma: " + palindroma("I topi non avevano nipoti"));
        System.out.println("Pari (0) o Dispari (1): " + pari_dispari(4));
        System.out.println("Fibonacci fino a 100: " + fibonacci(100));
    }

    /**
     * Calcola il prodotto degli elementi di un array di interi.
     */
    public static int prodotto(int[] lista) {
        if (lista == null || lista.length == 0) {
            return 0;
        }
        int risultato = 1;
        for (int v : lista) {
            risultato *= v;
        }
        return risultato;
    }

    /**
     * Calcola la media aritmetica degli elementi dell'array.
     */
    public static float media(int[] lista) {
        if (lista == null || lista.length == 0) {
            return 0.0f;
        }
        float somma = 0;
        for (int v : lista) {
            somma += v;
        }
        return somma / lista.length;
    }

    /**
     * Determina se un numero è pari o dispari.
     * @return 0 se pari, 1 se dispari
     */
    public static int pari_dispari(int n) {
        return (n % 2 == 0) ? 0 : 1;
    }

    /**
     * Conta il numero di vocali in una stringa.
     */
    public static int vocali(String s) {
        if (s == null) return 0;
        int count = 0;
        String vocaliStr = "aeiouAEIOU";
        for (int i = 0; i < s.length(); i++) {
            if (vocaliStr.indexOf(s.charAt(i)) != -1) {
                count++;
            }
        }
        return count;
    }

    /**
     * Verifica se una frase/parola è palindroma (ignorando spazi e maiuscole/minuscole).
     */
    public static boolean palindroma(String s) {
        if (s == null) return false;
        s = s.replaceAll("\\s+", "").toLowerCase();
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    /**
     * Genera e restituisce la sequenza di Fibonacci contenente i numeri <= n.
     */
    public static List<Integer> fibonacci(int n) {
        List<Integer> sequenza = new ArrayList<>();
        if (n < 0) return sequenza;

        int a = 0, b = 1;
        while (a <= n) {
            sequenza.add(a);
            int next = a + b;
            a = b;
            b = next;
        }
        return sequenza;
    }
}