N = int(input())
h = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}

move_l = input().split()
idx = [1, 1]


def is_save(n):
    return 1 if 0 < n < (N + 1) else 0


for m in move_l:
    tmp_x = idx[0] + h[m][0]
    tmp_y = idx[1] + h[m][1]
    if is_save(tmp_x) and is_save(tmp_y):
        idx = [tmp_x, tmp_y]

print(*idx, sep=" ")
