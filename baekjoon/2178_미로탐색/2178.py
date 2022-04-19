import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())

board = []
memo = [[n*m + 1 for _ in range(m + 1)] for _ in range(n + 1)]
re = n * m
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def is_safe(x, y):
    if (-1 < x < n and -1 < y < m) and board[x][y] == '1':
        return 1
    return 0


for _ in range(n):
    board.append(list(sys.stdin.readline()))

q = [(0, 0, 1)]


def bfs(q):
    global re
    x, y, c = q.pop(0)
    if x == n - 1 and y == m - 1:
        if c < re:
            re = c
        return

    board[x][y] = '0'
    if c < re:
        for i in range(4):
            if is_safe(x + dx[i], y + dy[i]):
                if memo[x + dx[i]][y + dy[i]] > c + 1:
                    memo[x + dx[i]][y + dy[i]] = c + 1
                    q.append((x + dx[i], y + dy[i], c + 1))

    if q:
        bfs(q)


bfs(q)
print(re)

# noti: dfs는 시간초과
#
# def dfs(x, y, c):
#     global re
#     if x == n - 1 and y == m - 1:
#         if re > c:
#             re = c
#         return
#
#     for i in range(4):
#         board[x][y] = '0'
#         if is_safe(x + dx[i], y + dy[i]):
#             dfs(x + dx[i], y + dy[i], c + 1)
#         board[x][y] = '1'
#
# dfs(0, 0, 0)
# print(re + 1)