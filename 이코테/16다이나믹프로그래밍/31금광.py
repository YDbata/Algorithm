t = int(input())

dx = [-1, 0, 1]


def max_n(x, y, lst, memo):
    # 종료 조건
    if memo[x][y] != -1:
        return memo[x][y]
    tmp_l = []
    for d in dx:
        if -1 < x + d < n:
            memo[x + d][y - 1] = max_n(x + d, y - 1, lst, memo)
            tmp_l.append(memo[x + d][y - 1])

    return max(tmp_l) + lst[x][y]


for _ in range(t):
    n, m = map(int, input().split())
    lst = [[0 for _ in range(m)] for _ in range(n)]
    memo = [[-1 for _ in range(m)] for _ in range(n)]
    for idx, num in enumerate(map(int, input().split())):
        if idx % m == 0:
            memo[idx // m][idx % m] = num

        lst[idx // m][idx % m] = num
    # 재귀
    re_l = []
    for i in range(n):
        re_l.append(max_n(i, m - 1, lst, memo))

    print(max(re_l))

'''
예시
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''