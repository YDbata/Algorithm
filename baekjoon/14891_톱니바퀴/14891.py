top = []
zero_loc = [0, 0, 0, 0]
loc = [0, 0, 0, 0]
tf = [0, 0, 0, 0]


def round_top(n):
    if n <= -1:
        return n + 8
    elif n >= 8:
        return n - 8

    return n


for _ in range(4):
    top.append(list(map(int, list(input()))))

for i in range(int(input())):
    tf = [0,0,0,0]
    # 바꿀 톱니와 방향 정하기
    n, m = map(int, input().split())
    loc[n - 1] = m
    tf[n - 1] = 1
    for j in range(n - 1, 3):
        if top[j][round_top(zero_loc[j] + 2)] != top[j + 1][round_top(zero_loc[j + 1] + 6)]:
            tf[j + 1] = 1
            loc[j + 1] = -loc[j]
        else:
            break

    for j in range(n - 1, 0, -1):
        if top[j][round_top(zero_loc[j] + 6)] != top[j - 1][round_top(zero_loc[j - 1] + 2)]:
            tf[j - 1] = 1
            loc[j - 1] = -loc[j]
        else:
            break

    # 돌리기
    for j in range(4):
        if tf[j] == 1:
            zero_loc[j] = round_top(zero_loc[j] - loc[j])

# zero 리스트 index로 더하기
re = 0
for i in range(4):
    re += top[i][zero_loc[i]]*(2**i)

print(re)
