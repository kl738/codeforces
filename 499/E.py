n, k = map(int,input().split())
v = list(map(int,input().split()))

def gcd(a,b):
	if a < b:
		return gcd(b,a)
	if b == 0:
		return a
	else:
		return gcd(b, a%b) 

g = v[0]
for i in range(1,n):
	g = gcd(g, v[i])

lst = set()
for i in range(k):
	lst.add(g*i % k)

lst = sorted(list(lst))
print(len(lst))
print(' '.join(map(str,lst)))