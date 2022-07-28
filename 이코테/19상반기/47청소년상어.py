import copy

dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
re = 0
board = [[[0, 0] for _ in range(4)] for _ in range(4)]
for x in range(4):
    tmp = list(map(int, input().split()))

    for y in range(4):
        board[x][y] = [tmp[y * 2], tmp[(y * 2) + 1]]  # 번호, 방향

# print(board)
q = []
for i in range(1, 17):
    for x in range(4):
        for y in range(4):
            if board[x][y][0] == i:
                q.append([x, y])

shark = [0, 0, board[0][0][1]]
q[board[0][0][0] - 1] = [-1, -1]
re = board[0][0][0]
board[0][0] = [-1, -1]  # 빈칸
t_board = board.copy


def is_safe(x, y):
    if -1 < x < 4 and -1 < y < 4:
        return 1
    return 0


def board_move(b, sh):
    global q
    for i in range(1, 17):
        x, y = q[i - 1]
        # print([x, y], board[x][y])
        if x == -1:
            continue
        dir = b[x][y][1] - 1
        for j in range(9):
            if is_safe(x + dx[dir], y + dy[dir]) and [x + dx[dir], y + dy[dir]] != sh[:2] and \
                    b[x + dx[dir]][y + dy[dir]][0] != -1:
                q[b[x][y][0] - 1], q[b[x + dx[dir]][y + dy[dir]][0] - 1] = q[b[x + dx[dir]][y + dy[dir]][0] - 1], q[
                    b[x][y][0] - 1]
                b[x + dx[dir]][y + dy[dir]], b[x][y] = b[x][y], b[x + dx[dir]][y + dy[dir]]
                b[x + dx[dir]][y + dy[dir]][1] = dir + 1
                break

            dir = (dir + 1) % 8
        # print(q)


# dfs
def dfs(sh, ab, sum_n):
    global re, q
    tmp_b = copy.deepcopy(ab)
    # tmp_q = copy.deepcopy(aq)
    print("시작", sh, sum_n, *tmp_b, sep="\n")
    board_move(tmp_b, sh)
    print("board", *tmp_b, sep="\n")
    c = 1
    dir = sh[2] - 1
    while is_safe(sh[0] + dx[dir] * c, sh[1] + dy[dir] * c):
        if tmp_b[sh[0] + dx[dir] * c][sh[1] + dy[dir] * c][0] != -1:
            tmp_f = tmp_b[sh[0] + dx[dir] * c][sh[1] + dy[dir] * c]
            tmp_b[sh[0] + dx[dir] * c][sh[1] + dy[dir] * c] = [-1, -1]
            tmp_q = copy.deepcopy(q)
            q[tmp_f[0] - 1] = [-1, -1]
            # sh = [sh[0] + dx[dir]*c, sh[1] + dy[dir]*c, sh[2]]
            print("전", *tmp_b, q, sh, sum_n, sep="\n")
            dfs([sh[0] + dx[dir] * c, sh[1] + dy[dir] * c, tmp_f[1]], tmp_b, sum_n + tmp_f[0])
            print("후", *tmp_b, q, sh, sep="\n")
            tmp_b[sh[0] + dx[dir] * c][sh[1] + dy[dir] * c] = tmp_f
            q = tmp_q
            # q[tmp_f[0] - 1] = [sh[0] + dx[dir]*c, sh[1] + dy[dir]*c]
        c += 1

    if re < sum_n:
        re = sum_n


print(q)
print(*board, sep="\n")
# board_move(board, shark)
# print(board[0][2])
# shark = [q[board[0][2][0] - 1][0],q[board[0][2][0] - 1][1], board[0][2][1]]
# q[board[0][2][0] - 1] = [-1, -1]
# board[0][2] = [-1, -1]
# print(shark)
# print(*board,q, sep="\n")
# board_move(board, shark)
# print(*board, sep="\n")

dfs(shark, board, re)
print(re)