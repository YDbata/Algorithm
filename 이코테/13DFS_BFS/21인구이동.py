# title: 인구이동

import sys
sys.setrecursionlimit(1000000)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 좌우상하

def is_save(x1, y1):
    if -1 < x1 < n and -1 < y1 < n:
        return 1
    return 0


def dfs(x, y):
    global idx, count
    ssum = 0
    for i in range(4):
        if is_save(x + dx[i], y + dy[i]) and (l <= abs(a[x][y] - a[x + dx[i]][y + dy[i]]) <= r):
            if a_idx[x + dx[i]][y + dy[i]] == 0:
                ssum += a[x + dx[i]][y + dy[i]]
                idx.append((x + dx[i], y + dy[i]))
                a_idx[x + dx[i]][y + dy[i]] = 1
                count += 1
                ssum += dfs(x + dx[i], y + dy[i])
    return ssum


if __name__ == "__main__":
    n, l, r = map(int, input().split())

    a = [list(map(int, input().split())) for i in range(n)]
    re = -1
    while True:
        flag = False
        re += 1
        a_idx = [[0 for i in range(n)] for j in range(n)]
        idx = []

        t = 1
        for ro in range(0, n, 1):
            if t == 0:
                t = 1
            else:
                t = 0

            for c in range(t, n, 2):
                print(a_idx, a)
                count = 1
                idx = []
                tsum = a[ro][c]
                if a_idx[ro][c] == 0:
                    idx = [(ro, c)]
                    a_idx[ro][c] = 1
                    tsum += dfs(ro, c)

                if tsum > a[ro][c]:
                    flag = True

                for index in idx:
                    a[index[0]][index[1]] = tsum // count

        if not flag:
            break

    print(re)
