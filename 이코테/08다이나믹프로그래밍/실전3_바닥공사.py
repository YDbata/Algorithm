N = int(input())

re_l = [0 for i in range(N + 1)]
re_l[0] = re_l[1] = 1

for i in range(2, N + 1):
    re_l[i] = (re_l[i - 1] + re_l[i - 2] * 2) % 796796

print(re_l[N])
