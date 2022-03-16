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


re = 0


def find(A, B):
    global D, re
    while check(A, B):
        D = (4 + (D - 1)) % 4  # 0북 1동 2남 3서
        tmp_dir = direct[D]
        if board[A + tmp_dir[0]][B + tmp_dir[1]] == 0:
            if board[A][B] == 0:
                re += 1
            board[A][B] = 2
            find(A + tmp_dir[0], B + tmp_dir[1])
            A += tmp_dir[0]
            B += tmp_dir[1]


    rD = (4 + (D - 2)) % 4
    if board[A + direct[rD][0]][B + direct[rD][1]] == 1:
        return re
    else:
        if board[A][B] == 0:
            re += 1
        board[A][B] = 2
        find(A + direct[rD][0], B + direct[rD][1])


find(A, B)


print(re)

# 다시 풀어보기
