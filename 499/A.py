n, k = map(int,input().split())
s = input()

s = ''.join(sorted(s))

def cost(c):
	return ord(c)-ord("a")+1
# print(cost("a"))
total = cost(s[0])
k -= 1
curr = 0
i = 1
while i < n:
	if k == 0:
		break
	if cost(s[i])-cost(s[curr]) >= 2:
		total += cost(s[i])
		curr = i 
		k -= 1
	i += 1
if k > 0:
	print(-1)
else:
	print(total)





