import secrets

# Publicly agreed upon prime number (p) and primitive root modulo p (g)
# These values should be large primes in real-world scenarios
p = 23  # Prime modulus
g = 5   # Primitive root modulo p

# Alice generates her private key and public key
alice_private = secrets.randbelow(p)
alice_public = pow(g, alice_private, p)

# Bob generates his private key and public key
bob_private = secrets.randbelow(p)
bob_public = pow(g, bob_private, p)

# Exchange public keys and compute the shared secret
alice_shared_secret = pow(bob_public, alice_private, p)
bob_shared_secret = pow(alice_public, bob_private, p)

# Output
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
