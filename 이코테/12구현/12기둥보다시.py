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
    # board = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    # board[0][:] = [0 for _ in range(n + 1)]
    answer = []
    for b in build_frame:
        if b[3] == 1:
            answer.append(b[:3])
            if b[2] == 0:
                if b[1] != 0 and [b[0] - 1, b[1], 1] not in answer and [b[0], b[1], 1] not in answer and [b[0], b[1] - 1, 0] not in answer:
                    answer.pop()

            else: # 보
                if [b[0], b[1] - 1, 0] not in answer and [b[0] + 1, b[1] - 1, 0] not in answer and ([b[0] - 1, b[1], 1] not in answer or [b[0] + 1, b[1], 1] not in answer):
                    answer.pop()
        if b[3] == 0:
            answer.remove(b[:3])

            for i in answer:
                if i[2] == 0:
                    if i[1] != 0 and [i[0] - 1, i[1], 1] not in answer and [i[0], i[1], 1] not in answer and [i[0], i[1] - 1, 0] not in answer:
                        # print("dd", i)
                        answer.append(b[:3])
                        break

                else:  # 보
                    if [i[0], i[1] - 1, 0] not in answer and [i[0] + 1, i[1] - 1, 0] not in answer and (
                            [i[0] - 1, i[1], 1] not in answer or [i[0] + 1, i[1], 1] not in answer):
                        # print("d", i)
                        answer.append(b[:3])
                        break
        # print(b, "\n", answer)
    answer.sort()
    return answer

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print()
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))