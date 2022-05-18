import heapq


def dij(s, dis, graph):
    q = []

    heapq.heappush(q, (0, s))
    dis[s] = 0
    while q:
        dist, node = heapq.heappop(q)

        if dis[node] < dist:
            continue

        for i in graph[node]:
            score = dist + i[1]
            if score < dis[i[0]]:
                dis[i[0]] = score
                heapq.heappush(q, (score, i[0]))


def solution(n, s, a, b, fares):
    graph = [[] for i in range(n + 1)]
    dis = [[98765432] * (n + 1) for _ in range(n + 1)]

    for f in fares:
        graph[f[0]].append(f[1:])
        graph[f[1]].append([f[0], f[2]])

    # 다익:개선
    for i in range(1, n + 1):
        dij(i, dis[i], graph)

    re = dis[s][a] + dis[s][b]
    for d in range(n + 1):
        if d < 98765432:
            if re > dis[s][d] + dis[d][a] + dis[d][b]:
                re = dis[s][d] + dis[d][a] + dis[d][b]

    return re