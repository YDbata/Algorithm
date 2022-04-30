import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
l = []
coun = 0
re = 0
q = []
two = []
zero = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def is_safe(x, y):
    if -1 < x < n and -1 < y < m:
        return 1
    return 0


def bfs(x, y, q):
    for i in range(4):
        if is_safe(x + dx[i], y + dy[i]) and board[x + dx[i]][y + dy[i]] == 0:
            q.append((x + dx[i], y + dy[i]))

    if q:
        tmp = q.pop(0)
        board[tmp[0]][tmp[1]] = 2
        l.append(tmp)
        bfs(tmp[0], tmp[1], q)


for x in range(n):
    for y in range(m):
        if board[x][y] == 2:
            two.append((x, y))
        elif board[x][y] == 0:
            zero.append((x, y))

len_z = len(zero)

for x in range(len_z - 2):
    board[zero[x][0]][zero[x][1]] = 1
    for y in range(x + 1, len_z - 1):
        board[zero[y][0]][zero[y][1]] = 1
        for z in range(y + 1, len_z):
            board[zero[z][0]][zero[z][1]] = 1
            for t in two:
                q.append(t)
            t = q.pop(0)
            bfs(t[0], t[1], q)
            re_tmp = sum(b.count(0) for b in board)
            for i in l:
                board[i[0]][i[1]] = 0
            l = []
            if re < re_tmp:
                re = re_tmp
            board[zero[z][0]][zero[z][1]] = 0
        board[zero[y][0]][zero[y][1]] = 0
    board[zero[x][0]][zero[x][1]] = 0

print(re)
