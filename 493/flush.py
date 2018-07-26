import sys

low, high = 1, 1000000

while low != high:
    mid = (low + high + 1)//2
    sys.stdout.write(str(mid)+"\n")
    sys.stdout.flush()
    result = sys.stdin.readline().strip()
    if result == "<":
        high = mid - 1
    else:
        low = mid
sys.stdout.write("! "+str(low)+"\n")
sys.stdout.flush()
