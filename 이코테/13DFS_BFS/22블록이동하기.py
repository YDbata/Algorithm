def is_safe(r, n, x, y):
    if -1 < r[0][0] + x < n and -1 < r[0][1] + y < n:
        if -1 < r[1][0] + x < n and -1 < r[1][1] + y < n:
            return 1
    return 0

def is_lotate_safe(dl, xl, r, b):
    if is_safe(r, len(b), dl[0], dl[1]) and b[r[xl][0] + dl[0]][r[xl][1]] == 0 and b[r[xl][0] + dl[0]][r[xl][1] + dl[1]] == 0:
        return 1
    return 0

def dfs(n, r, cnt, board):
    global re
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    dl = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
    dl_v = [[1, -1], [1, 1], [-1, -1], [-1, 1]]
    # print(r, cnt)
    if [n - 1, n - 1] in r:
        # print("OK")
        if re > cnt:
            re = cnt
    # 이동
    for i in range(4):
        # print(r, "m")
        if is_safe(r, n, dx[i], dy[i]) and board[r[0][0] + dx[i]][r[0][1] + dy[i]] == 0 and board[r[1][0] + dx[i]][r[1][1] + dy[i]] == 0:
            tmp = [[r[0][0] + dx[i], r[0][1] + dy[i]], [r[1][0] + dx[i], r[1][1] + dy[i]]]
            tmp.sort()
            board[r[0][0]][r[0][1]] = 1
            board[r[1][0]][r[1][1]] = 1
            dfs(n, tmp, cnt + 1, board)
            board[r[0][0]][r[0][1]] = 0
            board[r[1][0]][r[1][1]] = 0

    # 회전
    for i in range(4):

        if r[0][0] == r[1][0]:
            if is_lotate_safe(dl[i], (i + 1)//3, r, board):
                # print(r, "l")
                if (i + 1)//3:
                    tmp = [r[0], [r[1][0] + dl[i][0], r[1][1] + dl[i][1]]]
                else:
                    tmp = [[r[0][0] + dl[i][0], r[0][1] + dl[i][1]], r[1]]
                tmp.sort()
                board[r[0][0]][r[0][1]] = 1
                board[r[1][0]][r[1][1]] = 1
                dfs(n, tmp, cnt + 1, board)
                board[r[0][0]][r[0][1]] = 0
                board[r[1][0]][r[1][1]] = 0
        else:
            if is_lotate_safe(dl_v[i], (i + 1) // 3, r, board):
                # print(r, "l")
                if (i + 1) // 3:
                    tmp = [r[0], [r[1][0] + dl_v[i][0], r[1][1] + dl_v[i][1]]]
                else:
                    tmp = [[r[0][0] + dl_v[i][0], r[0][1] + dl_v[i][1]], r[1]]

                tmp.sort()
                board[r[0][0]][r[0][1]] = 1
                board[r[1][0]][r[1][1]] = 1
                dfs(n, tmp, cnt + 1, board)
                board[r[0][0]][r[0][1]] = 0
                board[r[1][0]][r[1][1]] = 0

    return


def solution(board):
    global re
    answer = 0

    robot = [[0, 0], [0, 1]]
    re = 987654321

    dfs(len(board), robot, 0, board)

    return re

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))