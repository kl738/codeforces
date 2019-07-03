#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    string s;
    cin >> s;
    int i = 0;
    int p = 0;
    vector<char> ret;
    while(p < n){
        ret.push_back(s[p]);
        i += 1;
        p += i;
    }
    for(int i = 0; i < ret.size(); i++){
        cout << ret[i];
    }
    cout << "\n";
}