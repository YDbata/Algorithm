exp = 0
scale = 2
loc = []

n = int(input())

board = []
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
visit = [[-1 for _ in range(n)] for _ in range(n)]

for x in range(n):
    board.append(list(map(int, input().split())))

    for y in range(n):
        if board[x][y] == 9:
            loc = [x, y]
            board[x][y] = 0

sec = 0
# print(fish, board)
while True:
    q = [loc]
    fq = []
    visit = [[-1 for _ in range(n)] for _ in range(n)]
    visit[loc[0]][loc[1]] = 0
    fish_e = [-1,-1,n*n]
    while q:
        tmp = q.pop(0)
        for i in range(4):
            if -1 < tmp[0] + dx[i] < n and -1 < tmp[1] + dy[i] < n:
                if board[tmp[0] + dx[i]][tmp[1] + dy[i]] <= scale:
                    if visit[tmp[0] + dx[i]][tmp[1] + dy[i]] == -1 or visit[tmp[0] + dx[i]][tmp[1] + dy[i]] > visit[tmp[0]][tmp[1]] + 1:
                        visit[tmp[0] + dx[i]][tmp[1] + dy[i]] = visit[tmp[0]][tmp[1]] + 1
                        q.append([tmp[0] + dx[i], tmp[1] + dy[i]])
                    if 0 < board[tmp[0] + dx[i]][tmp[1] + dy[i]] < scale:
                        if fish_e[0] == -1 or fish_e[2] > visit[tmp[0]][tmp[1]] + 1:
                            fish_e = [tmp[0] + dx[i], tmp[1] + dy[i], visit[tmp[0]][tmp[1]] + 1]
                        elif fish_e[2] == visit[tmp[0]][tmp[1]] + 1:
                            if fish_e[0] > tmp[0] + dx[i] or (fish_e[0] == tmp[0] + dx[i] and fish_e[1] > tmp[1] + dy[i]):
                                fish_e = [tmp[0] + dx[i], tmp[1] + dy[i], visit[tmp[0]][tmp[1]] + 1]

    if fish_e[0] == -1:
        break
    sec += fish_e[2]
    loc = fish_e[:-1]
    board[fish_e[0]][fish_e[1]] = 0
    if exp + 1 == scale:
        scale += 1
        exp = 0
    else:
        exp += 1

print(sec)
