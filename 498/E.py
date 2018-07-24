n, q = [int(x) for x in input().split()]
officers = [int(x) for x in input().split()]

class Node:
	def __init__(self, v):
		self.val = v
		self.children = []
	def addChild(self, n):
		self.children.append(n)

commander = Node(1)
lst = [None]
lst.append(commander)

for index, p_index in enumerate(officers):
	officer = Node(index+2)
	parent = lst[p_index]
	parent.addChild(officer)
	lst.append(officer)

def solve(u, k):
	start = lst[u]
	ret = []
	def dfs(start):
		ret.append(start)
		for child in start.children:
			dfs(child)
	dfs(start)
	if len(ret) < k:
		return -1
	else:
		return ret[k-1].val

for i in range(q):
	u, k = [int(x) for x in input().split()]
	print(solve(u,k))