#include <iostream>
#include <vector>
using namespace std;

int main() {
	vector<long long> v;
	long long two_power;
	for(int i = 0; i <= 32; ++i){
		two_power = (long long)1<<i;
		v.push_back(two_power);
	}	
	int t;
	long long n;
	long long sum;
	cin >> t;
	for(int i = 0; i < t; ++i){
		cin >> n;
		sum = n*(n+1)/2;
		for(int j = 0; j <= 32; j++){
			if(v[j] <= n) sum -= 2 * v[j];
		}		
		cout << sum << "\n";
	}	
}

