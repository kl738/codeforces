#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;

    for(int i = 0; i < n; i++){
        map<char, int> d;
        string s;
        cin >> s;
        for(int j = 0; j < s.size(); j++){
            d[s[j]] += 1;
        }
        if(d.size() == 1){
            cout << "-1" << "\n";
        }
        else{
            map<char, int>::iterator it;
            for(it = d.begin(); it != d.end(); it ++){
                for(int j = 0; j < it->second; j++){
                    cout << it->first;
                }
            }
            cout << "\n";
        }
    }
}