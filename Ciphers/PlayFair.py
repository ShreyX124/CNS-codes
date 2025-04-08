def create_matrix(key):
    key = ''.join(filter(str.isalpha, key.lower()))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    seen = set()
    matrix = []

    full_key = key + ''.join(c for c in alphabet if c not in key)

    idx = 0
    for i in range(5):
        row = []
        for j in range(5):
            while idx < len(full_key) and full_key[idx] in seen:
                idx += 1
            if idx < len(full_key):
                row.append(full_key[idx])
                seen.add(full_key[idx])
                idx += 1
        matrix.append(row)
    return matrix

def replacer(matrix, ch, encode=True):
    if not ch.isalpha():
        return ch
    ch = ch.lower()
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                shift = 1 if encode else -1
                return matrix[i][(j + shift) % 5]
    return ch

def encode(matrix, text):
    return ''.join(replacer(matrix, c, encode=True) for c in text.lower())

def decode(matrix, text):
    return ''.join(replacer(matrix, c, encode=False) for c in text.lower())

# === Main Logic ===
text = input("Enter the string: ")
key = input("Enter the key (no spaces): ")

matrix = create_matrix(key)

print("Matrix:")
for row in matrix:
    print(' '.join(row))

encoded_text = encode(matrix, text)
print("Encoded string:", encoded_text)

decoded_text = decode(matrix, encoded_text)
print("Decoded string:", decoded_text)
