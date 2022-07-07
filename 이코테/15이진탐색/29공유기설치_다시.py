n, c = map(int,input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()

s = 1
e = lst[-1] - lst[0]
re = 0

while s <= e:
    m = (s + e)//2
    value = lst[0]
    count = 1
    for i in range(1, n):
        if lst[i] >= value + m:
            value = lst[i]
            count += 1
    if count >= c:
        s = m + 1
        re = m
    else:
        e = m - 1

print(re)





# for i in range(m, -1, -1):
#