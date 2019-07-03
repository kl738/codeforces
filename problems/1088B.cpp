#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,k;
    cin >> n >> k;
    int a[n];
    set<int> s;
    for(int i = 0; i < n; i++){
        cin >> a[i];
        s.insert(a[i]);
    }
    vector<int> a2;
    for(auto it = s.begin(); it != s.end(); it++){
        a2.push_back(*it);
    }
    sort(a2.begin(),a2.begin());
    for(int i = 0; i < a2.size(); i++){
        if(k==0) break;
        if(i==0) cout << a2[i] << "\n";
        else{
            cout << a2[i]-a2[i-1] << "\n";
        }
        k--;
    }
    while(k>0){
        cout << 0 << "\n";
        k--;
    }
}