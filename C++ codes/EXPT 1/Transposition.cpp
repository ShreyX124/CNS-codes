#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main() {
    string a, b = "", key;
    cout << "Enter the string to be encrypted: ";
    getline(cin, a);
    cout << "Enter key: ";
    cin >> key;

    int n = key.length(); 
    int r = ceil((float)a.length() / n); 
    char m[r][n];
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < n; j++) {
            if (i * n + j < a.length()) {
                m[i][j] = a[i * n + j];
            } else {
                m[i][j] = '_'; 
            };
        }
    }
    for(int i=0;i<n;i++)
    {
        int q= key[i]-'0'-1;
        for(int j=0;j<r;j++)
        {
            b+=m[j][q];
        }
    }    
    cout<<b;
}