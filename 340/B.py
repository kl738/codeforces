n = int(input())
a = list(map(int,input().split()))

ones = []
for i in range(n):
    if a[i] == 1:
        ones.append(i)

if len(ones) == 0:
    print(0)
elif len(ones) == 1:
    print(1)
else:
    total = 1
    for i in range(1,len(ones)):
        total *= (ones[i] - ones[i-1])
    print(total)
