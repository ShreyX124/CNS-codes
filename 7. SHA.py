import hashlib

# Message to be hashed
message = "Hello Shreyansh, this is a SHA hash!".encode()

# SHA-1
sha1_hash = hashlib.sha1(message).hexdigest()
print("SHA-1 :", sha1_hash)

# SHA-256
sha256_hash = hashlib.sha256(message).hexdigest()
print("SHA-256:", sha256_hash)

# SHA-512
sha512_hash = hashlib.sha512(message).hexdigest()
print("SHA-512:", sha512_hash)
