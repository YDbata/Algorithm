import sys

n = int(input())
m = int(input())
inf = 100001*n
board = [[inf for _ in range(n)] for _ in range(n)]

for i in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    board[tmp[0] - 1][tmp[1] - 1] = min(board[tmp[0] - 1][tmp[1] - 1], tmp[2])

for i in range(n):
    board[i][i] = 0

for k in range(n):
    for x in range(n):
        for y in range(n):
            board[x][y] = min(board[x][y], board[x][k] + board[k][y])

for x in range(n):
    for y in range(n):
        if board[x][y] == inf:
            board[x][y] = 0

for i in range(n):
    print(*board[i], sep=" ")
