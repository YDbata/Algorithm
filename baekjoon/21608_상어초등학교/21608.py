n = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

board = [[0 for _ in range(n)] for _ in range(n)]
q = []
s_l = {}


def is_safe(x, y):
    if -1 < x < n and -1 < y < n:
        return 1
    return 0


def check(x, y, n, lst=[]):
    re = 0
    if n == 0:
        for i in range(4):
            if is_safe(x + dx[i], y + dy[i]) and board[x + dx[i]][y + dy[i]] == 0:
                re += 1

    else:
        for i in range(4):
            if is_safe(x + dx[i], y + dy[i]) and board[x + dx[i]][y + dy[i]] in lst:
                re += 1
    return re


for i in range(n ** 2):
    tmp = list(map(int, input().split()))
    q = []
    s = tmp[0]
    like_l = tmp[1:]
    s_l[s] = like_l
    like_n = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                xy = check(x, y, s, like_l)
                if xy == like_n:
                    q.append((x, y))
                elif xy > like_n:
                    q = [(x, y)]
                    like_n = xy
    # print("1", s, q)
    if len(q) > 1:
        # 2번 시작 : 빈칸
        blank_n = 0
        new_q = []
        for qn in range(len(q)):
            blank_t = check(q[qn][0], q[qn][1], 0)
            if blank_t == blank_n:
                new_q.append(q[qn])
            elif blank_t > blank_n:
                new_q = [q[qn]]
                blank_n = blank_t
        q = new_q
        # print("2", s, q)
        if len(q) > 1:
            # 3번 시작 : r, c가 가장 작은 칸
            q.sort(key=lambda t: (t[0], t[1]))

    board[q[0][0]][q[0][1]] = s
    # print("b", board)

# 만족도 조사
re = 0
for x in range(n):
    for y in range(n):
        tmp = 0
        for d in range(4):
            if is_safe(x + dx[d], y + dy[d]) and board[x + dx[d]][y + dy[d]] in s_l[board[x][y]]:
                tmp += 1
        if tmp:
            re += 10 ** (tmp - 1)
print(re)
