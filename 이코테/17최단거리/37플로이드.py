n = int(input())
m = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    tmp = list(map(int, input().split()))
    board[tmp[0] - 1][tmp[1] - 1] = tmp[2]

print(board)