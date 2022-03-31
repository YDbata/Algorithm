N, M = map(int, input().split())
num_l = [int(input()) for _ in range(N)]
num_l.sort(reverse=True) # 오름차순

count_l = [98765 for _ in range(10000)]
count_l[num_l[-1]] = 1

for i in num_l:
    count_l[i] = 1

for i in range(num_l[-1], M - num_l[-1] + 1):
    if count_l[i] != 98765:
        for c in num_l:
            if count_l[i + c] > count_l[i]:
                count_l[i + c] = count_l[i] + 1

if count_l[M] != 98765:
    print(count_l[M])
else:
    print(-1)
