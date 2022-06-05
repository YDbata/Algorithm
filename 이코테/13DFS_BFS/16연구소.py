import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
virus = []
re = 0
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def is_safe(x, y):
    if -1 < x < n and -1 < y < m:
        return 1
    return 0


def dfs(v, b):
    b[v[0]][v[1]] = 2
    for i in range(4):
        if is_safe(v[0] + dx[i], v[1] + dy[i]) and b[v[0] + dx[i]][v[1] + dy[i]] == 0:
            dfs((v[0] + dx[i], v[1] + dy[i]), b)


# 2찾기
for x in range(n):
    for y in range(m):
        if board[x][y] == 2:
            virus.append((x, y))

for x in range(n * m):
    if board[x // m][x % m] == 0:
        for y in range(x + 1, n * m):
            if board[y // m][y % m] == 0:
                for z in range(y + 1, n * m):
                    # 몫 : x 나머지 : y (x,y)
                    if board[z // m][z % m] == 0:
                        n_board = [i.copy() for i in board]
                        n_board[x // m][x % m] = 1
                        n_board[y // m][y % m] = 1
                        n_board[z // m][z % m] = 1
                        for v in virus:
                            dfs(v, n_board)
                        # print(n_board, board)
                        tmp = 0
                        for i in range(n):
                            tmp += n_board[i].count(0)

                        if tmp > re:
                            re = tmp
print(re)
