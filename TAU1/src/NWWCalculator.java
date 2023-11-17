import java.util.Scanner;

public class NWWCalculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Podaj pierwszą liczbę: ");
        int liczba1 = scanner.nextInt();

        System.out.print("Podaj drugą liczbę: ");
        int liczba2 = scanner.nextInt();

        int nww = obliczNWW(liczba1, liczba2);

        System.out.println("Najmniejsza wspólna wielokrotność: " + nww);
    }

    // Metoda obliczająca NWW dwóch liczb
    public static Integer obliczNWW(int a, int b) {
        if (a == 0 || b == 0) {
            return null; // Jeśli którakolwiek z liczb jest zerem, NWW jest zerem
        }

        int nwd = obliczNWD(a, b);
        return Math.abs(a / nwd) * Math.abs(b); // Zwróć nieujemną wartość NWW
    }

    // Metoda obliczająca NWD dwóch liczb (algorytm Euklidesa)
    public static Integer obliczNWD(int a, int b) {
        if (a == 0 && b == 0) {
            return null;
        }

        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}