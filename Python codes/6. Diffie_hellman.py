import secrets

# Function to perform Diffie-Hellman key exchange
def diffie_hellman(p, g, alice_private, bob_private):
    # Alice generates her public key
    alice_public = pow(g, alice_private, p)

    # Bob generates his public key
    bob_public = pow(g, bob_private, p)

    # Alice and Bob compute the shared secret
    alice_shared_secret = pow(bob_public, alice_private, p)
    bob_shared_secret = pow(alice_public, bob_private, p)

    # Output the results
    print("Public Parameters:")
    print("  Prime (p):", p)
    print("  Primitive Root (g):", g)

    print("\nAlice:")
    print("  Private Key:", alice_private)
    print("  Public Key:", alice_public)

    print("\nBob:")
    print("  Private Key:", bob_private)
    print("  Public Key:", bob_public)

    print("\nShared Secret:")
    print("  Computed by Alice:", alice_shared_secret)
    print("  Computed by Bob:  ", bob_shared_secret)

# Main function to take custom input
def main():
    # Display example input for the user
    print("Example input format:")
    print("  Prime number (p): A large prime number, e.g., 23")
    print("  Primitive root (g): A number such that g is a primitive root modulo p, e.g., 5")
    print("  Private keys: Random numbers, e.g., Alice's private key: 6, Bob's private key: 15")
    print("")

    # Input prime modulus (p) and primitive root modulo p (g)
    p = int(input("Enter a prime number p (e.g., 23): "))
    g = int(input("Enter a primitive root g modulo p (e.g., 5): "))

    # Input private keys for Alice and Bob
    alice_private = int(input("Enter Alice's private key (e.g., 6): "))
    bob_private = int(input("Enter Bob's private key (e.g., 15): "))

    # Perform Diffie-Hellman key exchange
    diffie_hellman(p, g, alice_private, bob_private)

if __name__ == "__main__":
    main()
