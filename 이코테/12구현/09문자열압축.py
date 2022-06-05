# https://programmers.co.kr/learn/courses/30/lessons/60057
def zip_s(st, n):
    len_s =  len(st)
    s_cnt = 1
    re = [0, st[:n]]
    count = 1
    for i in range(0, len_s - n + 1, n):
        if st[i:i + n] == re[count]:
            re[count - 1] += 1
        else:
            count += 2
            re.append(1)
            re.append(st[i:i + n])
    if len_s%n != 0:
        re.append(st[-(len_s%n):])
    return re

def solution(s):
    answer = 10000
    for i in range(1, len(s)//2 + 2):
        tmp = zip_s(s, i)
        # print(tmp, answer)
        m = tmp.count(1)
        tmp = ''.join(map(str, tmp))
        if len(tmp) - m < answer:
            answer = len(tmp) - m
    return answer