import java.math.*;
import java.util.*;

public class RSA {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the first prime number (p): ");
        int p = scanner.nextInt();
        
        System.out.print("Enter the second prime number (q): ");
        int q = scanner.nextInt();
        
        System.out.print("Enter the message to be encrypted (integer value): ");
        int msg = scanner.nextInt();
        
        int n = p * q;
        int z = (p - 1) * (q - 1);
        System.out.println("The value of z = " + z);
        
        int e;
        for (e = 2; e < z; e++) {
            if (gcd(e, z) == 1) {
                break;
            }
        }
        System.out.println("The value of e = " + e);
        
        int d = 0;
        for (int i = 0; i <= 9; i++) {
            int x = 1 + (i * z);
            if (x % e == 0) {
                d = x / e;
                break;
            }
        }
        System.out.println("The value of d = " + d);
        
        double c = (Math.pow(msg, e)) % n;
        System.out.println("Encrypted message is : " + c);
        
        BigInteger N = BigInteger.valueOf(n);
        BigInteger C = BigDecimal.valueOf(c).toBigInteger();
        BigInteger msgback = (C.pow(d)).mod(N);
        System.out.println("Decrypted message is : " + msgback);
        
        scanner.close();
    }

    static int gcd(int e, int z) {
        if (e == 0)
            return z;
        else
            return gcd(z % e, e);
    }
}
