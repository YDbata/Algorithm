# https://programmers.co.kr/learn/courses/30/lessons/60059

def is_safe(x, y, n):
    if -1 < x < n and -1 < y < n:
        return 1
    return 0


def lotation_90(x, y, n):
    return (y, n - x)


def solution(key, lock):
    len_l = len(lock)
    lock_z = [(x, y) for x in range(len_l) for y in range(len_l) if lock[x][y] == 0]
    len_lock = len(lock_z)
    key_z = [(x, y) for x in range(len(key)) for y in range(len(key)) if key[x][y] == 1]
    print(lock_z)
    if len(key_z) < len_lock:
        return False
    if len_lock == 0:
        return True

    for loc in lock_z:
        n_key_z = key_z
        for k in range(len(key_z)):
            for lo in range(4):
                tmp_x = loc[0] - n_key_z[k][0]
                tmp_y = loc[1] - n_key_z[k][1]
                tmp_key = [(i[0] + tmp_x, i[1] + tmp_y) for i in n_key_z]
                count_k = 0
                flag = 0
                for t in tmp_key:
                    if is_safe(t[0], t[1], len_l):
                        if lock[t[0]][t[1]] == 0:
                            count_k += 1
                        elif lock[t[0]][t[1]] == 1:
                            flag = 1
                            break
                # print(n_key_z, tmp_key)
                if count_k == len_lock and flag == 0:
                    return True

                n_key_z = [lotation_90(i[0], i[1], len(key) - 1) for i in n_key_z]

    return False