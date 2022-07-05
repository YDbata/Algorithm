n, c = map(int,input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()
m = (n - 1)//2

re = lst[-1] - lst[0]

q = [(m, 0, n)]
count = c - 1
while count > 0:
    print(q)
    middle = q.pop(0)
    minn = lst[middle[0]] - lst[(middle[1] + middle[0] - 1)//2]
    maxn = lst[(middle[0] + middle[2] - 1)//2] - lst[middle[0]]
    if minn < maxn:
        if re > minn:
            re = minn
    else:
        if re > maxn:
            re = maxn

    if (middle[1] + middle[0] - 1)//2 != middle[1] and (middle[1] + middle[0] - 1)//2 != middle[0]:
        q.append(((middle[1] + middle[0] - 1)//2, middle[1], middle[0]))
        count -= 1

    if (middle[0] + middle[2] - 1)//2 != middle[0] and (middle[1] + middle[0] - 1)//2 != middle[2]:
        q.append(((middle[0] + middle[2] - 1)//2, middle[0], middle[2]))
        count -= 1

    print("r", q, re, minn, maxn)


print(re)
