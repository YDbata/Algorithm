N, M = map(int, input().split())

A, B, D = map(int, input().split())

board = []

for n in range(N):
    board.append(list(map(int, input().split())))

direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def check(a, b):
    for d in direct:
        if board[a + d[0]][b + d[1]] == 0:
            return 1

    return 0


re = 1
while check(A, B):
    D = (4 + (D - 1)) % 4
    tmp_dir = direct[D]
    if board[A + tmp_dir[0]][B + tmp_dir[1]] == 0:
        board[A][B] = 2
        A += tmp_dir[0]
        B += tmp_dir[1]
        re += 1


print(re)
