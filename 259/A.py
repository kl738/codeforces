n = int(input())

spacing = n//2
nd = 1

while nd < n:
	row = "*" * spacing + "D" * nd + "*" * spacing
	print(row)
	spacing -= 1
	nd += 2

print("D"*n)
nd -= 2
spacing +=1

while nd >= 1:
	row = "*" * spacing + "D" * nd + "*" * spacing
	print(row)
	spacing += 1
	nd += -2