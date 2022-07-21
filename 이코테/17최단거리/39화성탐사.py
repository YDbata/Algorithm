import heapq

t = int(input())
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for _ in range(t):
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    graph = [[] for _ in range(n * n)]
    for x in range(n):
        for y in range(n):
            for k in range(4):
                if -1 < x + dx[k] < n and -1 < y + dy[k] < n:
                    graph[(x * n) + y].append((board[x][y], ((x + dx[k]) * n) + y + dy[k]))

    hq = []
    distance = [987654321]*(n*n)
    heapq.heappush(hq, (0, 0))
    distance[0] = 0
    # print(graph)
    while hq:
        cost, now = heapq.heappop(hq)
        if distance[now] < cost:
            continue

        for i in graph[now]:
            t_cost = cost + i[0]
            if t_cost < distance[i[1]]:
                distance[i[1]] = t_cost
                heapq.heappush(hq, (t_cost, i[1]))


    print(distance[n*n - 1] + board[n - 1][n - 1])