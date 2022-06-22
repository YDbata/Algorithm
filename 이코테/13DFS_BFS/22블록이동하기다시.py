from collections import deque

def solution(board):
    len_b = len(board)
    new_board = [[1 for _ in range(len_b + 2)] for _ in range(len_b + 2)]
    visit = [((1, 1), (1, 2))]

    for x in range(len_b):
        for y in range(len_b):
            new_board[x + 1][y + 1] = board[x][y]

    # bfs
    q = deque([((1, 1), (1, 2), 0)])
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    # print(new_board)
    while q:
        t_1, t_2, t_count = q.popleft()
        # print(t_1, t_2, t_count, q)

        if t_1 == (len_b, len_b) or t_2 == (len_b, len_b):
            return t_count
        # 갈 수 있는 방향 탐색 후 가능하면 q에 넣기
        # 이동
        new_q = []
        for i in range(4):
            if new_board[t_1[0] + dx[i]][t_1[1] + dy[i]] == 0 and new_board[t_2[0] + dx[i]][t_2[1] + dy[i]] == 0:
                new_q.append(((t_1[0] + dx[i], t_1[1] + dy[i]), (t_2[0] + dx[i], t_2[1] + dy[i])))

        # 회전
        if t_1[0] == t_2[0]:  # 가로
            if new_board[t_1[0] + dx[3]][t_1[1] + dy[3]] == 0 and new_board[t_2[0] + dx[3]][t_2[1] + dy[3]] == 0:  # 왼
                new_q.append(((t_1[0] - 1, t_1[1]), t_1))
                new_q.append(((t_2[0] - 1, t_2[1]), t_2))
            if new_board[t_1[0] + dx[2]][t_1[1] + dy[2]] == 0 and new_board[t_2[0] + dx[2]][t_2[1] + dy[2]] == 0:  # 오
                new_q.append((t_1, (t_1[0] + dx[2], t_1[1] + dy[2])))
                new_q.append((t_2, (t_2[0] + dx[2], t_2[1] + dy[2])))
        else:  # 세로
            if new_board[t_1[0] + dx[1]][t_1[1] + dy[1]] == 0 and new_board[t_2[0] + dx[1]][t_2[1] + dy[1]] == 0:  #
                new_q.append(((t_1[0] + dx[1], t_1[1] + dy[1]), t_1))
                new_q.append(((t_2[0] + dx[1], t_2[1] + dy[1]), t_2))
            if new_board[t_1[0] + dx[0]][t_1[1] + dy[0]] == 0 and new_board[t_2[0] + dx[0]][t_2[1] + dy[0]] == 0:
                new_q.append((t_1, (t_1[0] + dx[0], t_1[1] + dy[0])))
                new_q.append((t_2, (t_2[0] + dx[0], t_2[1] + dy[0])))

        for nq in new_q:
            if nq not in visit:
                visit.append(nq)
                q.append((nq[0], nq[1], t_count + 1))


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]]))
print(solution(
    [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))
print(solution(
    [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]))
print(solution(
    [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 0]]))
# print(solution([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
