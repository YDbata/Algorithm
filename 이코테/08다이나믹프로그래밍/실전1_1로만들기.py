N = int(input())
save_re = [0 for _ in range(N + 1)]

'''def num1making(n, count):
    if n <= 1:
        return 0
    else:
        re = N
        if n % 5 == 0:
            if save_re[n // 5] == 0:
                save_re[n // 5] = num1making(n // 5, count + 1)

            if re > save_re[n // 5] + 1:
                re = save_re[n // 5] + 1

        if n % 3 == 0:
            if save_re[n // 3] == 0:
                save_re[n // 3] = num1making(n // 3, count + 1)

            if re > save_re[n // 3] + 1:
                re = save_re[n // 3] + 1

        if n % 2 == 0:
            if save_re[n // 2] == 0:
                save_re[n // 2] = num1making(n // 2, count + 1)

            if re > save_re[n // 2] + 1:
                re = save_re[n // 2] + 1

        if n > 1:
            if save_re[n - 1] == 0:
                save_re[n - 1] = num1making(n - 1, count + 1)

            if re > save_re[n - 1] + 1:
                re = save_re[n - 1] + 1

        save_re[n] = re
        return re


num1making(N, 0)

print(save_re[N])'''

# 재귀는 힘들었다

for i in range(2, N + 1):
    save_re[i] = save_re[i - 1] + 1

    if i % 5 == 0:
        save_re[i] = min(save_re[i], save_re[i // 5] + 1)
    if i % 3 == 0:
        save_re[i] = min(save_re[i], save_re[i // 3] + 1)
    if i % 2 == 0:
        save_re[i] = min(save_re[i], save_re[i // 2] + 1)

print(save_re[N])
