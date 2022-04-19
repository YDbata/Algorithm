n = int(input())
m = int(input())

dfs_l = [[] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]
count = 0


def dfs(x, c):
    if visit[x] == 0:
        visit[x] = 1
        for i in dfs_l[x]:
            if visit[i] == 0:
                c = dfs(i, c + 1)
    return c


for _ in range(m):
    s, e = map(int, input().split())
    dfs_l[s].append(e)
    dfs_l[e].append(s)

print(dfs(1, 0))
