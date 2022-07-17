n, m = map(int, input().split())

inf = 10001*n
board = [[inf for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    board[a][b] = b

# 플로이설
for k in range(n):
    for a in range(n):
        for b in range(n):
            board[a][b] = min(board[a][b], board[a][k] + board[k][b])

print(board)
re = 0
for b in board:
    if b.count(inf) == 1:
        pass
