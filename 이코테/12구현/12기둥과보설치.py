#https://programmers.co.kr/learn/courses/30/lessons/60061

def is_safe(x, y, n):
    if -1< x < n + 1 and -1 < y < n + 1:
        return 1
    return 0

def ok_0(x, y, board):
    if board[x][y] != -1:
        return 1
    return 0

def ok_1(x, y, board, n):
    if board[x][y] == 0 or (is_safe(x, y - 1, n) and board[x][y - 1] == 0):
        return 1

    if ((is_safe(x, y - 1, n) and board[x][y - 1] > -1) and (
            is_safe(x, y + 1, n) and board[x][y + 1] > -1)):
        return 1
    return 0

def solution(n, build_frame):
    board = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    board[0][:] = [0 for _ in range(n + 1)]
    answer = []
    for b in build_frame:
        if b[3] == 1:
            tmp = board[b[1] + 1][b[0]]
            # board[b[1] + 1][b[0]] = b[2]
            if b[2] == 0: # 기둥인 경우
                # print(b, ok_0(b[1], b[0], board), board)
                if ok_0(b[1], b[0], board):
                    board[b[1] + 1][b[0]] = b[2]
                    answer.append(b[:3])
            if b[2] == 1: # 보
                if ok_1(b[1], b[0] + 1, board, n):
                    board[b[1]][b[0] + 1] = b[2]
                    answer.append(b[:3])

        if b[3] == 0:

            if b[2] == 1:
                tmp = board[b[1]][b[0] + 1]
                if [b[1] - 1, b[0] + 1, 0] in answer:
                    board[b[1]][b[0] + 1] = 0
                else:
                    board[b[1]][b[0] + 1] = -1

                bx, by = b[1], b[0] + 1
                dx, dy = [0, 0, 1, -1], [0, 2, 1, 1]

            else:
                tmp = board[b[1] + 1][b[0]]
                if [b[1] + 1, b[0] - 1, 1] in answer:
                    board[b[1] + 1][b[0]] = 1
                else:
                    board[b[1] + 1][b[0]] = -1
                bx, by = b[1] + 1, b[0]
                dx, dy = [1, 1, 2, 0], [-1, 1, 0, 0]

            print("d", board[b[1] + 1][b[0]])
            f = 0
            for i in range(4):
                print(b[1] + dx[i], b[0] + dy[i])
                if board[b[1] + dx[i]][b[0] + dy[i]] == 0:
                    if ok_0(b[1] + dx[i], b[0] + dy[i], board) == 0:
                        board[bx][by] = tmp
                        f = 1
                elif board[b[1] + dx[i]][b[0] + dy[i]] == 1:
                    if ok_1(b[1] + dx[i], b[0] + dy[i], board, n) == 0:
                        print("0", b[1] + dx[i], b[0] + dy[i])
                        board[bx][by] = tmp
                        f = 1

            if f == 0:
                for ai in range(len(answer)):
                    if answer[ai] == b[:3]:
                        del answer[ai]
                        break
        print(b, "\n", answer, board)
    answer.sort()
    return answer

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print()
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))