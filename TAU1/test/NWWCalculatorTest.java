import org.testng.annotations.Test;
import static org.junit.jupiter.api.Assertions.*;

public class NWWCalculatorTest {

    @Test
    public void testObliczNWW() {
        assertEquals(12, NWWCalculator.obliczNWW(4, 6));
        assertEquals(20, NWWCalculator.obliczNWW(5, 4));
        assertEquals(18, NWWCalculator.obliczNWW(9, 6));
        assertEquals(35, NWWCalculator.obliczNWW(5, 7));
    }

    @Test
    public void testObliczNWD() {
        assertEquals(2, NWWCalculator.obliczNWD(4, 6));
        assertEquals(1, NWWCalculator.obliczNWD(5, 4));
        assertEquals(3, NWWCalculator.obliczNWD(9, 6));
        assertEquals(1, NWWCalculator.obliczNWD(5, 7));
        assertEquals(10, NWWCalculator.obliczNWD(0, 10));
    }

    @Test
    public void testObliczNWWZer() {
        assertEquals(null, NWWCalculator.obliczNWW(0, 10));
        assertEquals(null, NWWCalculator.obliczNWW(10, 0));
    }

    @Test
    public void testObliczNWDZer() {
        assertEquals(10, NWWCalculator.obliczNWD(0, 10));
        assertEquals(7, NWWCalculator.obliczNWD(7, 0));
    }

    @Test
    public void testObliczNWWUjemne() {
        assertEquals(12, NWWCalculator.obliczNWW(-4, 6));
        assertEquals(20, NWWCalculator.obliczNWW(5, -4));
        assertEquals(18, NWWCalculator.obliczNWW(-9, -6));
        assertEquals(35, NWWCalculator.obliczNWW(-5, 7));
    }

    @Test
    public void testCzyNWWNieJestUjemne() {
        assertTrue(NWWCalculator.obliczNWW(4, 6) > 0);
        assertTrue(NWWCalculator.obliczNWW(-4, 6) > 0);
    }

    @Test
    public void testCzyNWDNieJestUjemne() {
        assertFalse(NWWCalculator.obliczNWD(4, 6) < 0);
        assertFalse(NWWCalculator.obliczNWD(-4, 6) < 0);
    }

    @Test
    public void testCzyNWWNotNull() {
        assertNotNull(NWWCalculator.obliczNWW(4, 6));
    }

    @Test
    public void testCzyNWDNotNull() {
        assertNotNull(NWWCalculator.obliczNWD(4, 6));
    }

    @Test
    public void testCzyNWWNull() {
        assertNull(NWWCalculator.obliczNWW(0, 0));
    }

    @Test
    public void testCzyNWDNull() {
        assertNull(NWWCalculator.obliczNWD(0, 0));
    }

    @Test
    public void testCzyNWWNotEquals() {
        assertNotEquals(10, NWWCalculator.obliczNWW(4, 6));
    }

    @Test
    public void testCzyNWDNotEquals() {
        assertNotEquals(3, NWWCalculator.obliczNWD(4, 6));
    }
}