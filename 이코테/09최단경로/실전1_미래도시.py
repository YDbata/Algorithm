N, M = map(int, input().split())
edge = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    edge[s][e] = 1
    edge[e][s] = 1

x, k = map(int, input().split())


def road(s, e):
    q = []
    for i in range(1, N + 1):
        if edge[s][i] == 1:
            if i == e:
                return 1
            else:
                q.append([s, i, 1])

    while q and s != q[0][1]:
        for i in range(1, N + 1):
            if edge[q[0][1]][i] == 1:
                if i != e and q[0][0] != i:
                    q.append([q[0][1], i, q[0][2] + 1])
                elif i == e:
                    return q[0][2] + 1

        del q[0]

    return -1


kr = road(1, k)
xr = road(k, x)
if kr > 0 and xr > 0:
    print(kr + xr)
else:
    print(-1)
