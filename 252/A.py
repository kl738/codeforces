n, d = list(map(int, input().split()))
songs = list(map(int, input().split()))

time = 0
jokes = 0
overtime = False
while True:
    if len(songs) == 0:
        jokes += (d-time)//5
        break
    s = songs.pop()
    if time + s > d:
        overtime = True
        break
    else:
        time += s
    if len(songs) > 0:
        jokes += 2
        time += 10

if overtime:
    print(-1)
else:
    print(jokes)
