## 수정중

n, m = map(int, input().split())

maps = []
shark = []
re = 0
tmp = 2500
dx = (1, -1, 0, 0, 1, 1, -1, -1)
dy = (0, 0, 1, -1, -1, 1, -1, 1)
def bfs(xt, yt, count):
    global tmp

    if maps[xt][yt]:
        if count < tmp:
            tmp = count
    else:
        pass

for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(m):
        if maps[i][j]:
            shark.append((i, j))

for x in range(n):
    for y in range(m):
        if maps[x][y] == 0:
            tmp = 2500
            bfs(x, y, 0)
            if tmp > re:
                re = tmp

print(re)