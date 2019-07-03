#include <bits/stdc++.h>
using namespace std;

char getChar(int x){
    return (char)('a' + x);
}
int main(){
    int t;
    cin >> t;
    for(int i = 0; i < t; i++){
        int n, k;
        cin >> n >> k;
        int p = 0;
        while(p<n){
            cout << getChar(p%k);
            p++;
        }
        cout << "\n";
    }
}
