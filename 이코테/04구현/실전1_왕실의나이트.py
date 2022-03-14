# 스피드런

dir = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

loc = input()

loc_x = ord(loc[0]) - ord('a') + 1
loc_y = int(loc[1])


def is_save(n):
    return 1 if 0 < n < 9 else 0


re = 0
for d in dir:
    if is_save(loc_x + d[0]) and is_save(loc_y + d[1]):
        re += 1

print(re)
