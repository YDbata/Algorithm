# python으로 시간초과
# pypy3로 정답
n, m = map(int, input().split())

board = []

re = 0
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

for _ in range(n):
    board.append(list(map(int, input().split())))

visit = [[0 for _ in range(m)] for _ in range(n)]


def is_safe_sh(x, s):
    if -1 < x < s - 2:
        return 1
    return 0


def is_safe(x, y):
    if -1 < x < n and -1 < y < m and visit[x][y] == 0:
        return 1
    return 0


def fill_sum(x, y, c, sum_t):
    global re
    if c == 4:
        if re < sum_t:
            re = sum_t
    else:
        for i in range(4):
            if is_safe(x + dx[i], y + dy[i]):
                visit[x + dx[i]][y + dy[i]] = 1
                fill_sum(x + dx[i], y + dy[i], c + 1, sum_t + board[x + dx[i]][y + dy[i]])
                visit[x + dx[i]][y + dy[i]] = 0
    return


# c는 1로 시작
for x in range(n):
    for y in range(m):
        visit[x][y] = 1
        fill_sum(x, y, 1, board[x][y])
        visit[x][y] = 0

# ㅜ 모양
dx2 = [[(-1, 1), (1, 1)], [(1, 1), (1, -1)]]
for x in range(n):
    for y in range(m):
        if is_safe_sh(y, m):
            sum_n = board[x][y] + board[x][y + 1] + board[x][y + 2]
            if is_safe(x + dx2[0][0][0], y + dx2[0][0][1]) and is_safe(x + dx2[0][1][0], y + dx2[0][1][1]):
                if board[x + dx2[0][0][0]][y + dx2[0][0][1]] > board[x + dx2[0][1][0]][y + dx2[0][1][1]]:
                    tmp = sum_n + board[x + dx2[0][0][0]][y + dx2[0][0][1]]
                else:
                    tmp = sum_n + board[x + dx2[0][1][0]][y + dx2[0][1][1]]
            elif is_safe(x + dx2[0][0][0], y + dx2[0][0][1]):
                tmp = sum_n + board[x + dx2[0][0][0]][y + dx2[0][0][1]]
            elif is_safe(x + dx2[0][1][0], y + dx2[0][1][1]):
                tmp = sum_n + board[x + dx2[0][1][0]][y + dx2[0][1][1]]
            else:
                tmp = 0

            if re < tmp:
                re = tmp

        if is_safe_sh(x, n):
            sum_n = board[x][y] + board[x + 1][y] + board[x + 2][y]
            if is_safe(x + dx2[1][0][0], y + dx2[1][0][1]) and is_safe(x + dx2[1][1][0], y + dx2[1][1][1]):
                if board[x + dx2[1][0][0]][y + dx2[1][0][1]] > board[x + dx2[1][1][0]][y + dx2[1][1][1]]:
                    tmp = sum_n + board[x + dx2[1][0][0]][y + dx2[1][0][1]]
                else:
                    tmp = sum_n + board[x + dx2[1][1][0]][y + dx2[1][1][1]]
            elif is_safe(x + dx2[1][0][0], y + dx2[1][0][1]):
                tmp = sum_n + board[x + dx2[1][0][0]][y + dx2[1][0][1]]
            elif is_safe(x + dx2[1][1][0], y + dx2[1][1][1]):
                tmp = sum_n + board[x + dx2[1][1][0]][y + dx2[1][1][1]]
            else:
                tmp = 0

            if re < tmp:
                re = tmp

print(re)
