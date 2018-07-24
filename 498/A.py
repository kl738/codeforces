n = int(input())
lst = [int(x) for x in input().split()]
for i, v in enumerate(lst):
	if v%2==0:
		lst[i] = v-1
lst = [str(x) for x in lst]
print(' '.join(lst))