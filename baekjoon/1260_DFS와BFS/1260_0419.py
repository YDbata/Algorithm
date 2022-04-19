n, m, v = map(int, input().split())

l = [[] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    l[s].append(e)
    l[e].append(s)

for i in l:
    i.sort()


def dfs(x):
    if visit[x] == 0:
        visit[x] = 1
        print(x, end=" ")
        for i in l[x]:
            dfs(i)


def bfs(q):
    tmp = q.pop(0)
    if visit[tmp] == 0:
        visit[tmp] = 1
        print(tmp, end=" ")
        for i in l[tmp]:
            if visit[i] == 0:
                q.append(i)

    if q:
        bfs(q)


dfs(v)
print()
# print(*visit, sep=" ")
visit = [0 for _ in range(n + 1)]
bfs([v])
# print(*visit, sep=" ")

