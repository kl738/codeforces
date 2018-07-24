n = int(input())
s1 = input()
s2 = input()

d = {}
for i in range(10):
	d[i] = 0
for c in s2:
	d[int(c)] += 1

# min flicks
flicks_saved = 0
for c in s1:
	digit = int(c)
	for i in range(digit,10):
		if d[i] > 0:
			flicks_saved += 1
			d[i] -= 1
			break
print(n-flicks_saved)


d = {}
for i in range(10):
	d[i] = 0
for c in s2:
	d[int(c)] += 1

# max flicks 
flicks_inflicted = 0
for c in s1:
	digit = int(c)
	for i in range(digit + 1, 10):
		if d[i] > 0:
			flicks_inflicted += 1
			d[i] -= 1
			break
print(flicks_inflicted)
