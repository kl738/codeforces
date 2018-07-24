m, n = list(map(int,input().split()))

exp = 0
for k in range(1, m+1):
	prob = ((k/m)**n) *(1-((k-1)/k)**n)
	exp += prob * k
print(exp)