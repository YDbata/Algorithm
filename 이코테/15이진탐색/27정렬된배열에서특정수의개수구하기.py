n,x = map(int, input().split())
l = list(map(int, input().split()))

def bi(x, s, e):
    global min_s, max_s
    # print(s, e)
    m = (s + e - 1)//2
    if m == s or m == e:
        if min_s > m:
            min_s = m
        if max_s < m:
            max_s = m
    else:
        if l[m] == x:
            bi(x, s, m)
            bi(x, m + 1, e)
        elif l[m] > x:
            bi(x, s, m)
        elif l[m] < x:
            bi(x, m + 1, e)


min_s, max_s =  n - 1, 0
bi(x, 0, n)
# print(max_s, min_s)
if min_s - max_s == 0:
    print(-1)
else:
    print(max_s - min_s)

