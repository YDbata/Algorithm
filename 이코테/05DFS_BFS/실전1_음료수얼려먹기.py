N, M = map(int, input().split())
board = []


def is_save(numx, numy):
    return 1 if -1 < numx < N and -1 < numy < M else 0


def fill(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    board[x][y] = 1
    for i in range(4):
        if is_save(x + dx[i], y + dy[i]):
            if board[x + dx[i]][y + dy[i]] == 0:
                fill(x + dx[i], y + dy[i])


for n in range(N):
    board.append(list(map(int, list(input()))))

count = 0
for n in range(N):
    for m in range(M):
        if board[n][m] == 0:
            fill(n, m)
            count += 1
print(count)
