import sys

n,m,k,x = map(int, input().split())
visit = [-1 for _ in range(n + 1)]
node = [[] for _ in range(n + 1)]
for _ in range(m):
    p, s = map(int, sys.stdin.readline().split())
    node[p].append(s)

q = [x]
visit[x] = 0
while q:
    tmp = q.pop(0)
    if visit[tmp] < k:
        for i in node[tmp]:
            if visit[i] == -1 or visit[i] > visit[tmp] + 1:
                visit[i] = visit[tmp] + 1
                q.append(i)

re = [i for i in range(n + 1) if visit[i] == k]

if re:
    re.sort()
    print(*re, sep="\n")
else:
    print(-1)