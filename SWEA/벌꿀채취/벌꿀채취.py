import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.


re = 0
def find_max(x, y, m, c, s):
    global re
    if c < 0:
        if re < s - pow(board[x][y - 1],2):
            re = s - pow(board[x][y - 1],2)
            # print(x, y, "re", re)
    elif m == 0:
        if re < s:
            re = s
            # print(x, y, "re", re)
    else:
        for i in range(y, y + m):
            find_max(x, i + 1, m - (i - y + 1), c - board[x][i], s + pow(board[x][i], 2))


for test_case in range(1, T + 1):
    board = []

    n, m, c = map(int, input().split())
    max_sum = [[] for _ in range(n)]

    for i in range(n):
        board.append(list(map(int, input().split())))

    for x in range(n):
        for y in range(n - m + 1):
            re = 0
            if sum(board[x][y:y+m]) <= c:
                max_sum[x].append(sum(map(lambda x : x**2, board[x][y:y+m])))
            else:
                find_max(x, y, m, c, 0)
                max_sum[x].append(re)

    rre = 0
    for x in range(n):
        for y in range(n - m + 1):
            for x2 in range(x, n):
                if x == x2 and y + m < n - m + 1:
                    for y2 in range(y + m, n - m + 1):
                        # print(x, y, x2, y2, max_sum)
                        if max_sum[x][y] + max_sum[x2][y2] > rre:
                            rre = max_sum[x][y] + max_sum[x2][y2]
                elif x != x2:
                    for y2 in range(n - m + 1):
                        # print(x, y, x2, y2, max_sum)
                        if max_sum[x][y] + max_sum[x2][y2] > rre:
                            rre = max_sum[x][y] + max_sum[x2][y2]

    print("#"+str(test_case), rre)



