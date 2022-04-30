n, M = map(int, input().split())
q = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

A = [list(map(int, input().split())) for _ in range(n)]

dx = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
dx_1 = [1,3,5,7]


def do_safe(n, x, y, d, s):
    if x + s * dx[d][0] < 0:
        x = (x + s * dx[d][0]) % n
    elif x + s * dx[d][0] > n - 1:
        x = (x + s * dx[d][0]) % n
    else:
        x += s * dx[d][0]

    if y + s * dx[d][1] < 0:
        y = (y + s * dx[d][1]) % n
    elif y + s * dx[d][1] > n - 1:
        y = (y + s * dx[d][1]) % n
    else:
        y += s * dx[d][1]
    return (x, y)


def is_safe(x, y):
    if -1 < x < n and -1 < y < n:
        return 1
    return 0


for m in range(M):
    d, s = map(int, input().split())

    # 이동 # 물양 증가
    for q_n in range(len(q)):
        q[q_n] = ((q[q_n][0] + s*dx[d - 1][0])%n, (q[q_n][1] + s*dx[d - 1][1])%n) #do_safe(n, q[q_n][0], q[q_n][1], d - 1, s)

        A[q[q_n][0]][q[q_n][1]] += 1

    # 물복사
    for q_n in range(len(q)):
        count_n = 0
        for dx_t in dx_1:
            if is_safe(q[q_n][0] + dx[dx_t][0], q[q_n][1] + dx[dx_t][1]) \
                    and A[q[q_n][0] + dx[dx_t][0]][q[q_n][1] + dx[dx_t][1]] != 0:
                count_n += 1

        A[q[q_n][0]][q[q_n][1]] += count_n
    # 새로운 구름 채우기(new_q)
    new_q = []
    for x in range(n):
        for y in range(n):
            if A[x][y] > 1 and (x, y) not in q:
                A[x][y] -= 2
                new_q.append((x, y))

    q = new_q

re = 0
for i in range(n):
    re += sum(A[i])

print(re)