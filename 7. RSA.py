from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Generate RSA key pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

print("🔑 Private Key:")
print(private_key.decode())

print("\n🔓 Public Key:")
print(public_key.decode())

# Encrypt a message using the public key
message = b'Hello Shreyansh, this is RSA encryption!'
recipient_key = RSA.import_key(public_key)
cipher_rsa = PKCS1_OAEP.new(recipient_key)
ciphertext = cipher_rsa.encrypt(message)

print("\n🔐 Encrypted message (ciphertext):")
print(ciphertext)

# Decrypt the message using the private key
private_key_obj = RSA.import_key(private_key)
cipher_rsa = PKCS1_OAEP.new(private_key_obj)
decrypted_message = cipher_rsa.decrypt(ciphertext)

print("\n📬 Decrypted message:")
print(decrypted_message.decode())
