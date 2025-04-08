#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

// Function to perform modular exponentiation
long long modExp(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) // If exp is odd, multiply base with result
            result = (result * base) % mod;
        base = (base * base) % mod; // Square the base
        exp /= 2;
    }
    return result;
}

int main() {
    srand(time(0)); // Seed for random number generation
    
    // User input for public parameters
    long long p, g;
    cout << "Enter a prime number (p): ";
    cin >> p;
    cout << "Enter a primitive root modulo p (g): ";
    cin >> g;
    
    cout << "Publicly shared values: p = " << p << ", g = " << g << endl;
    
    // User input for private keys
    long long a, b;
    cout << "Enter Alice's private key: ";
    cin >> a;
    cout << "Enter Bob's private key: ";
    cin >> b;
    
    // Compute public keys
    long long A = modExp(g, a, p); // Alice's public key
    long long B = modExp(g, b, p); // Bob's public key
    
    cout << "Alice's public key: " << A << endl;
    cout << "Bob's public key: " << B << endl;
    
    // Exchange public keys and compute shared secret
    long long sharedSecretAlice = modExp(B, a, p); // Alice computes shared secret
    long long sharedSecretBob = modExp(A, b, p);   // Bob computes shared secret
    
    cout << "Alice's computed shared secret: " << sharedSecretAlice << endl;
    cout << "Bob's computed shared secret: " << sharedSecretBob << endl;
    
    if (sharedSecretAlice == sharedSecretBob)
        cout << "Key exchange successful! Shared secret: " << sharedSecretAlice << endl;
    else
        cout << "Key exchange failed!" << endl;
    
    return 0;
}