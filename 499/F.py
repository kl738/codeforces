n = int(input())
op = [""] * n
inflag = [True] * n
args = [list() for _ in range(n)]
for i in range(n):
    inp = list(input().split())
    # print(inp)
    if inp[0] == "AND" or inp[0] == "XOR" or inp[0] == "OR":
        op[i] = inp[0]
        inflag[i] = False
        args[i].append(int(inp[1])-1)
        args[i].append(int(inp[2])-1)
    elif inp[0] == "NOT":
        op[i] = inp[0]
        inflag[i] = False
        args[i].append(int(inp[1])-1)
    elif inp[0] == "IN":
        op[i] = inp[0]
        inflag[i] = True
        args[i].append(int(inp[1]))

def flip(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
#recursive implementation, probably won't work because of python :/
def dfs(root):
    if op[root] == "IN":
        return args[root][0]
    elif op[root] == "NOT":
        return flip(dfs(args[root][0]))
    elif op[root] == "AND":
        return dfs(args[root][0]) & dfs(args[root][1])
    elif op[root] == "OR":
        return dfs(args[root][0]) | dfs(args[root][1])
    elif op[root] == "XOR":
        return dfs(args[root][0]) ^ dfs(args[root][1])

ans = []
curr = -1
for i in range(n):
    if inflag[i]:
        if curr == -1:
            curr = i
            args[i][0] = flip(args[i][0])
        else:
            args[curr][0] = flip(args[curr][0])
            args[i][0] = flip(args[i][0])
            curr = i
        ans.append(str(dfs(0)))
print(''.join(ans))
