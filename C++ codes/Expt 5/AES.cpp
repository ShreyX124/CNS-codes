#include <iostream>
#include <cstring>
#include <iomanip>

using namespace std;

const int BLOCK_SIZE = 16;

void simpleXorEncrypt(const unsigned char* plaintext, unsigned char* ciphertext, const unsigned char* key) {
    for (int i = 0; i < BLOCK_SIZE; i++) {
        ciphertext[i] = plaintext[i] ^ key[i];
    }
}

void simpleXorDecrypt(const unsigned char* ciphertext, unsigned char* decryptedtext, const unsigned char* key) {
    for (int i = 0; i < BLOCK_SIZE; i++) {
        decryptedtext[i] = ciphertext[i] ^ key[i];
    }
}

int main() {
    unsigned char key[BLOCK_SIZE];
    unsigned char plaintext[BLOCK_SIZE];
    unsigned char ciphertext[BLOCK_SIZE];
    unsigned char decryptedtext[BLOCK_SIZE];

    cout << "Enter a 16-character key: ";
    cin.read(reinterpret_cast<char*>(key), BLOCK_SIZE);
    cin.ignore();

    cout << "Enter a 16-character plaintext: ";
    cin.read(reinterpret_cast<char*>(plaintext), BLOCK_SIZE);

    simpleXorEncrypt(plaintext, ciphertext, key);
    cout << "Encrypted text: ";
    for (int i = 0; i < BLOCK_SIZE; i++) {
        cout << hex << setw(2) << setfill('0') << static_cast<int>(ciphertext[i]);
    }
    cout << endl;

    simpleXorDecrypt(ciphertext, decryptedtext, key);
    decryptedtext[BLOCK_SIZE - 1] = '\0'; // Ensure null-termination
    cout << "Decrypted text: " << decryptedtext << endl;

    return 0;
}
