import sys

if __name__=="__main__":
    v, e = map(int, input().split())
    k = int(input())
    v_list = [[] for _ in range(v + 1)]
    visited = [0 for _ in range(v + 1)]
    weight = [999999 for _ in range(v + 1)]
    for _ in range(v):
        u, nd, w = map(int, sys.stdin.readline().split())
        v_list[u].append((nd, w))

    visited[k] = 1
    weight[k] = 0
    for _ in range(v):
        for i in v_list[k]:
            if weight[k] + i[1] < weight[i[0]]:
                weight[i[0]] = weight[k] + i[1]

        min_w = 999999
        min_idx = k
        for i in range(1, v + 1):
            if weight[i] < min_w and visited[i] == 0:
                min_w = weight[i]
                min_idx = i

        visited[min_idx] = 1
        k = min_idx

    for p in weight[1:]:
        if p >= 999999:
            print('INF')
        else:
            print(p)


