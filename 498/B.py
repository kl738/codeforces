n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

temp = sorted(a, reverse = True)
g = []
for i in range(k):
	g.append(temp[i])
print(sum(g))
curr = 0
i = 0
while i < len(a):
	curr += 1
	if a[i] in g: 
		g.remove(a[i])
		if len(g) == 0:
			print(curr+len(a)-i-1)
		else:
			print(curr, end = " ")
		curr = 0 
	i += 1