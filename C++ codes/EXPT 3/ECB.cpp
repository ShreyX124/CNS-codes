#include <iostream>
#include <vector>
#include <cstring>
#include <iomanip>

// Simulated block cipher encryption function (XOR-based)
std::vector<uint8_t> encryptBlock(const std::vector<uint8_t>& plaintext, const std::vector<uint8_t>& key) {
    std::vector<uint8_t> ciphertext(plaintext.size());
    for (size_t i = 0; i < plaintext.size(); ++i) {
        ciphertext[i] = plaintext[i] ^ key[i % key.size()];
    }
    return ciphertext;
}

// XOR is symmetric, so decryption is the same as encryption
std::vector<uint8_t> decryptBlock(const std::vector<uint8_t>& ciphertext, const std::vector<uint8_t>& key) {
    return encryptBlock(ciphertext, key);
}

// ECB Encryption
std::vector<uint8_t> ecbEncrypt(const std::vector<uint8_t>& plaintext, const std::vector<uint8_t>& key) {
    size_t blockSize = 8;
    std::vector<uint8_t> ciphertext;

    for (size_t i = 0; i < plaintext.size(); i += blockSize) {
        std::vector<uint8_t> block(plaintext.begin() + i, plaintext.begin() + std::min(i + blockSize, plaintext.size()));
        if (block.size() < blockSize) {
            block.resize(blockSize, 0); // Padding
        }
        std::vector<uint8_t> encryptedBlock = encryptBlock(block, key);
        ciphertext.insert(ciphertext.end(), encryptedBlock.begin(), encryptedBlock.end());
    }

    return ciphertext;
}

// ECB Decryption
std::vector<uint8_t> ecbDecrypt(const std::vector<uint8_t>& ciphertext, const std::vector<uint8_t>& key) {
    size_t blockSize = 8;
    std::vector<uint8_t> plaintext;

    for (size_t i = 0; i < ciphertext.size(); i += blockSize) {
        std::vector<uint8_t> block(ciphertext.begin() + i, ciphertext.begin() + i + blockSize);
        std::vector<uint8_t> decryptedBlock = decryptBlock(block, key);
        plaintext.insert(plaintext.end(), decryptedBlock.begin(), decryptedBlock.end());
    }

    return plaintext;
}

// Function to convert hexadecimal string to byte vector
std::vector<uint8_t> hexStringToBytes(const std::string& hex) {
    std::vector<uint8_t> bytes;
    for (size_t i = 0; i < hex.length(); i += 2) {
        std::string byteString = hex.substr(i, 2);
        bytes.push_back(static_cast<uint8_t>(std::stoi(byteString, nullptr, 16)));
    }
    return bytes;
}

// Function to convert byte vector to hex string
std::string bytesToHexString(const std::vector<uint8_t>& bytes) {
    std::ostringstream hexStream;
    for (uint8_t byte : bytes) {
        hexStream << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(byte);
    }
    return hexStream.str();
}

int main() {
    std::vector<uint8_t> key = {0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6}; // 64-bit key

    // Get user input for plaintext
    std::string inputText;
    std::cout << "Enter text to encrypt: ";
    std::getline(std::cin, inputText);

    // Convert input string to byte vector
    std::vector<uint8_t> plaintext(inputText.begin(), inputText.end());

    // Encrypt
    std::vector<uint8_t> ciphertext = ecbEncrypt(plaintext, key);
    std::string hexCiphertext = bytesToHexString(ciphertext);
    std::cout << "Encrypted (Hex): " << hexCiphertext << std::endl;

    // Get user input for ciphertext
    std::string inputCiphertext;
    std::cout << "Enter hex string to decrypt: ";
    std::getline(std::cin, inputCiphertext);

    // Convert hex string to byte vector
    std::vector<uint8_t> receivedCiphertext = hexStringToBytes(inputCiphertext);

    // Decrypt
    std::vector<uint8_t> decryptedText = ecbDecrypt(receivedCiphertext, key);
    std::cout << "Decrypted Text: ";
    for (uint8_t byte : decryptedText) {
        std::cout << static_cast<char>(byte);
    }
    std::cout << std::endl;

    return 0;
}
