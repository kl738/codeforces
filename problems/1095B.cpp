#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    int a[n];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    sort(a, a+n);
    int l = 0;
    int r = n-1;

    int linstability = a[r-1] - a[l];
    int rinstability = a[r] - a[l+1];

    cout << min(linstability, rinstability) << "\n";
}