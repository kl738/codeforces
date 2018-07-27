n = int(input())
m = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
start = m

if b[0]-1 <= 0:
	print(-1)
else:
	m += m/(b[0]-1)
	flag = True
	for i in range(n-1,0,-1):
		if a[i] - 1 <= 0:
			flag = False
			print(-1)
			break
		else:
			m += m/(a[i]-1)
		if b[i] - 1 <= 0:
			flag = False
			print(-1)
			break
		else:
			m += m/(b[i]-1)
	if flag:
		if a[0] - 1 <= 0:
			print(-1)
		else:
			m += m/(a[0]-1)
			print(m-start)