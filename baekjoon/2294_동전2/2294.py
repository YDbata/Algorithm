def combi(cn, start, ck, count):
    global re
    if ck == k:
        if re > count:
            re = count
        return count
    else:
        for c in range(start, cn):
            if ck + dong[c] > k:
                continue
            else:
                combi(cn, c, ck + dong[c], count + 1)
    return count

if __name__=="__main__":
    re = 100000
    n, k = map(int, input().split())
    dong = set()
    for _ in range(n):
        tmp = int(input())
        if tmp <= k:
            dong.add(tmp)

    dong = sorted(list(dong), reverse=True)

    combi(len(dong), 0, 0, 0)
    print(re)