n = int(input())
nums = list(map(int,input().split()))

first = 0 
for i in range(0,n-1):
	if nums[i] > nums[i+1]:
		first = i + 1

nums = nums[first:] + nums[:first]

flag = True
for i in range(n-1):
	if nums[i] > nums[i+1]:
		flag = False

if flag:
	print((n-first)%n)
else:
	print(-1)