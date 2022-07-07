n = int(input())

lst = list(map(int, input().split()))

count_n = 1
cur = lst[0]
for i in range(1, n):
    if lst[i] < cur:
        count_n += 1
    else:
        c = 0
        while lst[i] > lst[i - c - 1]:
            c += 1
        count_n += 1 - c
    # print(i, count_n, cur)
    cur = lst[i]

print(n - count_n)
