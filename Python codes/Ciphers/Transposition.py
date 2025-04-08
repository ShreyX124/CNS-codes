import math

def columnar_transposition_encrypt(text, key):
    b = ""
    n = len(key)
    r = math.ceil(len(text) / n)

    # Create a matrix and fill it row-wise
    matrix = [['_' for _ in range(n)] for _ in range(r)]
    for i in range(len(text)):
        row = i // n
        col = i % n
        matrix[row][col] = text[i]

    # Build cipher text column-wise based on the key order
    for i in range(n):
        q = int(key[i]) - 1  # Convert key character to column index
        for j in range(r):
            b += matrix[j][q]

    return b

# === Main Logic ===
a = input("Enter the string to be encrypted: ")
key = input("Enter key (e.g. 3142): ")
cipher = columnar_transposition_encrypt(a, key)
print(cipher)
