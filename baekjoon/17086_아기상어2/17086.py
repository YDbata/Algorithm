n, m = map(int, input().split())

maps = []
shark = []
re = 0
for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(m):
        if maps[i][j]:
            shark.append((i, j))

for x in range(n):
    for y in range(m):
        if maps[x][y] == 0:
            tmp = 2500
            for s in shark:
                xt = abs(x - s[0])
                yt = abs(y - s[1])
                if xt > yt:
                    if tmp > xt:
                        tmp = xt
                else:
                    if tmp > yt:
                        tmp = yt

            if tmp > re:
                re = tmp

print(re)
