N, M, C = map(int, input().split())

edge = [[int(1e9) for _ in range(N + 1)] for _ in range(N + 1)]
dist = [int(1e9)]*(N + 1)

for _ in range(M):
    s, e, r = map(int, input().split())
    edge[s][e] = r

q = []
re = 0
dist[C] = 0
count = 0
for i in range(1, N + 1):
    if edge[C][i] < int(1e9):
        q.append(i)
        if dist[i] > edge[C][i]:
            dist[i] = edge[C][i]
            count += 1
        if re < dist[i]:
            re = dist[i]

while q:
    for i in range(1, N + 1):
        if edge[q[0]][i] < int(1e9):
            q.append(i)
            if dist[i] > edge[C][i]:
                if dist[i] == int(1e9):
                    count += 1
                dist[i] = edge[C][i]

            if re < dist[i]:
                re = dist[i]
    del q[0]

print(count, re)