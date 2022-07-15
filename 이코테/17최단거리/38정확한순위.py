n, m = map(int, input().split())

board = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    board[a][b] = b

print(board)