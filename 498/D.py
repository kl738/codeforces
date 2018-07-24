n = int(input())
s1 = input()
s2 = input()

low, high = 0, n-1

gcount = 0
while high >= low:
	d = {}
	lst = []
	if high > low:
		lst.append(s1[low])
		lst.append(s1[high])
		lst.append(s2[low])
		lst.append(s2[high])
	elif high == low:
		lst.append(s1[low])
		lst.append(s2[low])
	for c in lst:
		if d.get(c) == None:
			d[c] = 1
		else:
			d[c] += 1
	if len(lst) == 2 and 1 in d.values():
		gcount += 1
	elif len(lst) == 4 and  3 in d.values():
		gcount += 1
	elif len(lst) == 4 and len(d) == 3 and s1[low]==s1[high]:
		gcount += 2
	elif len(lst) == 4 and len(d) == 3:
		gcount += 1
	elif len(lst) == 4 and len(d) == 4:
		gcount += 2
	high -= 1
	low += 1

print(gcount)