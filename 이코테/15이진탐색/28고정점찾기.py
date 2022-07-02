n = int(input())
lst = list(map(int, input().split()))

m = (n - 1)//2
s, e = 0, n - 1
while m != lst[m]:
    if m <= s or m >= e - 1:
        break
    if m > lst[m]:
        s = m
        m = (m + e)//2
    else:
        e = m
        m = (m - 1)//2

if m == lst[m]:
    print(m)
else:
    print(-1)