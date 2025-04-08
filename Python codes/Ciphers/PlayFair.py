def create_matrix(key):
    key = ''.join(filter(str.isalpha, key.lower().replace('j', 'i')))
    alphabet = 'abcdefghiklmnopqrstuvwxyz'  # 'j' is typically omitted in 5x5 matrices
    seen = set()
    matrix = []

    full_key = key + ''.join(c for c in alphabet if c not in key)
    
    idx = 0
    for i in range(5):
        row = []
        while len(row) < 5 and idx < len(full_key):
            if full_key[idx] not in seen:
                row.append(full_key[idx])
                seen.add(full_key[idx])
            idx += 1
        matrix.append(row)
    return matrix

def find_position(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
    return None, None

def replacer(matrix, ch, encode=True):
    if not ch.isalpha():
        return ch
    ch = ch.lower().replace('j', 'i')  # unify j → i
    row, col = find_position(matrix, ch)
    if row is not None:
        shift = 1 if encode else -1
        return matrix[row][(col + shift) % 5]
    return ch

def encode(matrix, text):
    return ''.join(replacer(matrix, c, encode=True) for c in text)

def decode(matrix, text):
    return ''.join(replacer(matrix, c, encode=False) for c in text)

# === Main Logic ===
text = input("Enter the string: ")
key = input("Enter the key (no spaces): ")

matrix = create_matrix(key)

print("\nMatrix:")
for row in matrix:
    print(' '.join(row))

encoded_text = encode(matrix, text)
print("\nEncoded string:", encoded_text)

decoded_text = decode(matrix, encoded_text)
print("Decoded string:", decoded_text)
