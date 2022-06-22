import sys

sys.setrecursionlimit(10 ** 7)

def is_safe(r, n, x, y, e):
    if -1 < r[0] + x < n and -1 < r[1] + y < n:
        if -1 < r[0] + x + e[0] < n and -1 < r[1] + y + e[1] < n:
            return 1
    return 0


def is_lotate_safe(dl, r, b, e):
    if e[0] == 0:
        # 가로
        if dl[0] > 0:
            if -1 < r[0] + 1 < len(b) and -1 < r[1] + e[1] < len(b):
                if b[r[0] + 1][r[1]] == 0 and b[r[0] + 1][r[1] + e[1]] == 0:
                    return 1
        else:
            if -1 < r[0] - 1 < len(b) and -1 < r[1] + e[1] < len(b):
                if b[r[0] - 1][r[1]] == 0 and b[r[0] - 1][r[1] + e[1]] == 0:
                    return 1
    else:
        # 세로
        if dl[1] > 0:
            if -1 < r[0] + e[0] < len(b) and -1 < r[1] + 1 < len(b):
                if b[r[0]][r[1] + 1] == 0 and b[r[0] + e[0]][r[1] + 1] == 0:
                    return 1
        else:
            if -1 < r[0] + e[0] < len(b) and -1 < r[1] - 1 < len(b):
                if b[r[0]][r[1] - 1] == 0 and b[r[0] + e[0]][r[1] - 1] == 0:
                    return 1

    return 0


def dfs(n, r, ext, cnt, board):
    global re
    # print(cnt)
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    dl = [[1, 0], [-1, 0], [1, 1], [-1, 1]]
    dl_v = [[0, 1], [0, -1], [-1, 1], [-1, -1]]
    # print(r, cnt, board, ext)

    if [n - 1, n - 1] == r or [n - 1, n - 1] == [r[0] + ext[0], r[1] + ext[1]]:
        # print("OK")
        if re > cnt:
            re = cnt
    else:
        # 이동
        for i in range(4):
            # print(r, "m")
            if is_safe(r, n, dx[i], dy[i], ext) and board[r[0] + dx[i]][r[1] + dy[i]] == 0 and \
                    board[r[0] + dx[i] + ext[0]][r[1] + dy[i] + ext[1]] == 0:
                tmp = [r[0] + dx[i], r[1] + dy[i]]
                board[r[0]][r[1]] = 1
                board[r[0] + ext[0]][r[1] + ext[1]] = 1
                dfs(n, tmp, ext, cnt + 1, board)
                board[r[0]][r[1]] = 0
                board[r[0] + ext[0]][r[1] + ext[1]] = 0

        # 회전
        for i in range(4):
            if ext[0] == 0:
                if is_lotate_safe(dl[i], r, board, ext):
                    tmp = r.copy()
                    if dl[1] != 0:
                        tmp[1] += ext[1]
                    board[r[0]][r[1]] = 1
                    board[r[0] + ext[0]][r[1] + ext[1]] = 1
                    dfs(n, tmp, [dl[i][0], 0], cnt + 1, board)
                    board[r[0]][r[1]] = 0
                    board[r[0] + ext[0]][r[1] + ext[1]] = 0
            else:
                if is_lotate_safe(dl_v[i], r, board, ext):
                    # print(r, "l")
                    tmp = r.copy()
                    if dl[0] != 0:
                        tmp[0] += ext[0]

                    board[r[0]][r[1]] = 1
                    board[r[0] + ext[0]][r[1] + ext[1]] = 1
                    dfs(n, tmp, [0, dl_v[i][1]], cnt + 1, board)
                    board[r[0]][r[1]] = 0
                    board[r[0] + ext[0]][r[1] + ext[1]] = 0

    return


def solution(board):
    global re
    answer = 0

    robot = [0, 0]
    extra = [0, 1]
    re = 987654321

    dfs(len(board), robot, extra, 0, board)

    return re


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
print(solution([[0,0,0], [0,0,0], [0,0,0]]))
print(solution([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
