n, b = map(int,input().split())
v = list(map(int,input().split()))

costs = []

odds = 0
evens = 0
for i in range(n-1):
    if v[i] % 2 == 0:
        evens += 1
    else:
        odds += 1
    if odds == evens and odds != 0 and i != (n-1):
        costs.append(abs(v[i+1]-v[i]))
        odds = 0
        evens = 0

count = 0
acc = 0
for cost in sorted(costs):
    if acc + cost <= b:
        count += 1
        acc = acc + cost
    else:
        break
print(count)
