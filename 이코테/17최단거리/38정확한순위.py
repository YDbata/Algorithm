n, m = map(int, input().split())

inf = 10001*n
board = [[inf for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = b

# 플로이설
for k in range(n):
    for a in range(n):
        for b in range(n):
            board[a][b] = min(board[a][b], board[a][k] + board[k][b])

# print(board)
re = 0
for i in range(n):
    tmp = n - board[i].count(inf)
    for j in range(n):
        if board[j][i] != inf:
            tmp += 1

    if tmp >= n - 1:
        re += 1

print(re)

'''
알게 된것
초기화 가능
숫자 카운트시 if문
if board[i][j] != inf or board[j][i] != inf:
    tmp += 1
'''