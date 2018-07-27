x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

px = [x1,x2,x3]
py = [y1,y2,y3]
x = set(px)
y = set(py)

if len(x) == 1 or len(y) == 1:
    print(1)
elif len(x) == 2 and len(y) == 2:
    print(2)
elif len(x) == 2:
    wanted = -1
    for i in range(3):
        if px.count(px[i]) == 1:
            wanted = i
    value = py[wanted]
    py.pop(wanted)
    if value > max(py) or value < min(py):
        print(2)
    else:
        print(3)
elif len(y) ==2:
    wanted = -1
    for i in range(3):
        if py.count(py[i]) == 1:
            wanted = i
    value = px[wanted]
    px.pop(wanted)
    if value > max(px) or value < min(px):
        print(2)
    else:
        print(3)
else:
    print(3)
