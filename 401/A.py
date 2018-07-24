n = int(input())
ball = int(input())

n = n % 6

while n > 0:
	if n % 2 == 1:
		if ball == 0:
			ball = 1
		elif ball == 1:
			ball = 0
	elif n % 2 == 0:
		if ball == 1:
			ball = 2
		elif ball == 2:
			ball = 1
	n -= 1

print(ball)
