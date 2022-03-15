N, M = map(int, input().split())

board = []
re = 40000


def is_save(x, y):
    return 1 if -1 < x < N and -1 < y < M else 0


def find(x, y, count):
    global re

    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    if (x, y) == (N - 1, M - 1):
        re = min(re, count)
        return 0

    for i in range(4):
        if is_save(x + dx[i], y + dy[i]) and board[x + dx[i]][y + dy[i]] == 1:
            board[x][y] = 2
            find(x + dx[i], y + dy[i], count + 1)
            board[x][y] = 1

    return 0


for n in range(N):
    board.append(list(map(int, list(input()))))

find(0, 0, 0)

print(re + 1)
