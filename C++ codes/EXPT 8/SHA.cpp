#include <iostream>
#include <vector>
#include <cstring>
#include <sstream>
#include <iomanip>
#include <cstdint>

using namespace std;

// Constants for SHA-256
const uint32_t K[] = {
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
};

// Rotate right macro
#define ROTR(x, n) ((x >> n) | (x << (32 - n)))

string sha256(const string& message) {
    vector<uint8_t> data(message.begin(), message.end());
    uint64_t original_length = data.size() * 8;
    data.push_back(0x80);
    
    while ((data.size() * 8) % 512 != 448) {
        data.push_back(0);
    }
    
    for (int i = 7; i >= 0; --i) {
        data.push_back((original_length >> (i * 8)) & 0xFF);
    }
    
    uint32_t H[] = {
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    };
    
    for (size_t i = 0; i < data.size(); i += 64) {
        uint32_t W[64];
        for (int j = 0; j < 16; ++j) {
            W[j] = (data[i + j * 4] << 24) | (data[i + j * 4 + 1] << 16) |
                   (data[i + j * 4 + 2] << 8) | (data[i + j * 4 + 3]);
        }
        
        for (int j = 16; j < 64; ++j) {
            uint32_t s0 = ROTR(W[j-15], 7) ^ ROTR(W[j-15], 18) ^ (W[j-15] >> 3);
            uint32_t s1 = ROTR(W[j-2], 17) ^ ROTR(W[j-2], 19) ^ (W[j-2] >> 10);
            W[j] = W[j-16] + s0 + W[j-7] + s1;
        }
        
        uint32_t a = H[0], b = H[1], c = H[2], d = H[3];
        uint32_t e = H[4], f = H[5], g = H[6], h = H[7];
        
        for (int j = 0; j < 64; ++j) {
            uint32_t S1 = ROTR(e, 6) ^ ROTR(e, 11) ^ ROTR(e, 25);
            uint32_t ch = (e & f) ^ (~e & g);
            uint32_t temp1 = h + S1 + ch + K[j] + W[j];
            uint32_t S0 = ROTR(a, 2) ^ ROTR(a, 13) ^ ROTR(a, 22);
            uint32_t maj = (a & b) ^ (a & c) ^ (b & c);
            uint32_t temp2 = S0 + maj;
            
            h = g;
            g = f;
            f = e;
            e = d + temp1;
            d = c;
            c = b;
            b = a;
            a = temp1 + temp2;
        }
        
        H[0] += a; H[1] += b; H[2] += c; H[3] += d;
        H[4] += e; H[5] += f; H[6] += g; H[7] += h;
    }
    
    stringstream ss;
    for (int i = 0; i < 8; ++i) {
        ss << hex << setw(8) << setfill('0') << H[i];
    }
    
    return ss.str();
}

int main() {
    string message;
    cout<<"Enter the message to tbe hashed: ";
    getline(cin, message);
    cout << "SHA-256 Hash: " << sha256(message) << endl;
    return 0;
}
