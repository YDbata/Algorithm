import heapq

n, m = map(int, input().split())

inf = 987654321
graph = [[] for i in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

distance = [inf]*(n + 1)
distance[1] = 0
q = []
heapq.heappush(q, (0, 1))
# print(graph)
while q:
    cost, now = heapq.heappop(q)
    if distance[now] < cost:
        continue

    for i in graph[now]:
        if distance[i] > cost + 1:
            distance[i] = cost + 1
            heapq.heappush(q, (cost + 1, i))

re, M = [], 0
for i in range(1, n + 1):
    if distance[i] > M:
        re = [i]
        M = distance[i]
    elif distance[i] == M:
        re.append(i)

print(re[0], M, len(re))