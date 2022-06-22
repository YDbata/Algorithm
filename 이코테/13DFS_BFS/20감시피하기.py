from itertools import combinations

n = int(input())
dx, dy = [0,0,1,-1], [-1,1,0,0]
re = "NO"
board = [input().split() for _ in range(n)]
tee = []
stud = []


def is_safe(x, y):
    if -1 < x < n and -1 < y < n:
        return 1
    return 0


# 선생찾기, 학생
for x in range(n):
    for y in range(n):
        if board[x][y] == 'T':
            tee.append((x, y))
        elif board[x][y] == 'S':
            stud.append((x, y))

combi = combinations(range(n * n), 3)
# (0, 1, 2) , (0,1,3) ... (n*n - 2, -1 n*n)
for x, y, z in combi:
    if board[x // n][x % n] == 'X' and board[y // n][y % n] == 'X' and board[z // n][z % n] == 'X':
        tmp = set()
        re = "YES"
        board[x // n][x % n] = 'O'
        board[y // n][y % n] = 'O'
        board[z // n][z % n] = 'O'
        for t in tee:
            for d in range(4):
                c = 1
                while is_safe(t[0] + dx[d]*c, t[1] + dy[d]*c) and board[t[0] + dx[d]*c][t[1] + dy[d]*c] != 'O':
                    if board[t[0] + dx[d]*c][t[1] + dy[d]*c] == 'S':
                        re = "NO"
                        # print(x, y, z, d, c, t[0] + (dx[d]*c), t[1] + (dy[d]*c), t)
                        break
                    c += 1

        # if re == "NO":
        #     print(x, y, z)
        board[x // n][x % n] = 'X'
        board[y // n][y % n] = 'X'
        board[z // n][z % n] = 'X'
        if re == "YES":
            break

print(re)
