n,k = map(int,input().split())
s = input()

s = ''.join(sorted(s))
def cost(c):
	return ord(c) - ord('a') + 1

curr = 0
total = cost(s[curr])
count = 1

for i in range(1,n):
	if count == k:
		break
	if cost(s[i]) - cost(s[curr]) >= 2:
		total += cost(s[i])
		count += 1
		curr = i
if count == k:
	print(total)
else:
	print(-1)