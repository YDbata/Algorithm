
def dfs(node):
    for nd in range(1, n + 1):
        if visit[nd] == 0 and node_list[node][nd] == 1:
            print(nd, end=" ")
            visit[nd] = 1
            dfs(nd)

if __name__=="__main__":
    n, m, v = map(int, input().split())

    node_list = [[0 for _ in range(n + 1)] for i in range(n + 1)]
    visit = [0 for i in range(n + 1)]
    bfs_stack = [v]

    for _ in range(m):
        p, s = map(int, input().split())
        node_list[p][s] = 1
        node_list[s][p] = 1

    print(v, end=" ")
    visit[v] = 1
    dfs(v)

    print()
    visit = [0 for i in range(n + 1)]
    while bfs_stack:
        s_node = bfs_stack.pop(0)
        print(s_node, end=" ")
        visit[s_node] = 1
        for y in range(1, n + 1):
            if visit[y] == 0 and node_list[s_node][y] == 1:
                bfs_stack.append(y)
                visit[y] = 1