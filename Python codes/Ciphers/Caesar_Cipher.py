def caesar_cipher(text):
    result = ""
    for char in text:
        if char.islower():
            result += chr(((ord(char) + 3 - ord('a')) % 26) + ord('a'))
        else:
            result += chr(((ord(char) + 3 - ord('A')) % 26) + ord('A'))
    return result

# Input from user
a = input("Enter the String: ")
encrypted = caesar_cipher(a)
print(encrypted)
