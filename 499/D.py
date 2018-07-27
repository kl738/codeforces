from sys import stdin, stdout
m, n = map(int, stdin.readline().split())

truths = [True] * n 
for i in range(n):
	stdout.write("1\n")
	stdout.flush()
	res = stdin.readline().strip()
	if res == "0":
		exit()
	elif res == "1":
		truths[i] = True
	elif res == "-1":
		truths[i] = False

div = 30 // n
truths = truths * (div + 1)

low, high = 1, m
for i in range(30):
	mid = (low+high+1)//2
	stdout.write(str(mid)+"\n")
	stdout.flush()
	res = stdin.readline().strip()
	if res == "0":
		exit()
	if res == "-2":
		exit()
	if truths[i]:
		if res == "1":
			low = mid
		else:
			high = mid -1
	if not truths[i]:
		if res == "1":
			high = mid -1
		else:
			low = mid