n,x,y = map(int,input().split())
s = input()

# x = cost of reverse
# y = cost of invert

chains = 0

zero = False
for i in range(n):
    if not zero and s[i] == "0":
        zero = True
    elif not zero and s[i] == "1":
        continue
    elif zero and s[i] == "0":
        continue
    elif zero and s[i] == "1":
        chains += 1
        zero = False
if zero:
    chains += 1

if chains == 0:
    print(0)
else:
    min_cost = 99999999999999999999999999
    for n_invert in range(1,chains+1):
        n_reverse = chains - n_invert
        cost = n_reverse * x + n_invert * y
        min_cost = min(min_cost, cost)
    print(min_cost)
