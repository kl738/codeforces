n, q = map(int,input().split())
officers = map(int,input().split())

s = [[] for _ in range(n)]
c = [0] * n

for i,v in enumerate(officers):
	s[v-1].append(i+1)
print("Sucessors",s)

traversal = []
def dfs(root):
	traversal.append(root)
	c[root] = 1
	for child in s[root]:
		dfs(child)
		c[root] += c[child]

dfs(0)
print("Counts",c)
print("Dfs traversl",traversal)


# answer = ""
for _ in range(q):
	u, k = map(int,input().split())
	start = traversal.index(u-1)
	if k <= c[start]:
		# answer += (str(traversal[start+k-1]+1) + "\n")
		print(str(traversal[start+k-1]+1))

	else:
		# answer += "-1\n"
		print(-1)
# print(answer)
