#title:로봇청소기

n,m = map(int, input().split())

r, c, d = map(int , input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dr = ((-1, 0),(0, 1),(1,0),(0,-1)) # 북, 동, 남, 서
board[r][c] = 2 # 0 청소전 1 벽 2 청소후
result = 1
def is_save(x, y):
    try:
        if board[x][y] != 1:
            pass
        return 1
    except:
        return 0

def move(r, c, d):
    global result

    count = 0
    while count != 4:
        d -= 1
        if d == -1:
            d = 3

        if is_save(r + dr[d][0], c + dr[d][1]):
            if board[r + dr[d][0]][c + dr[d][1]] == 0:
                r, c = r + dr[d][0], c + dr[d][1]
                board[r][c] = 2
                count = 0
                # d += 1
                result += 1
            else:
                count += 1

    return r, c, d

while True:
    r,c,d = move(r,c,d)
    if board[r - dr[d][0]][c - dr[d][1]] != 1:
        r, c = r - dr[d][0], c - dr[d][1]
        # n, m, d = move(n,m,d)
    else:
        break

print(result)