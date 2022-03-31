# 다이나믹 프로그래밍

'다이나믹프로그래밍'은 동적계획법이라고도 하며<br>
메모리 공간을 더 사용하면서 시간을 비약적으로 줄이는 방법중에 하나이다.

### 실전1_1로만들기
재귀
```python
N = int(input())
save_re = [0 for _ in range(N + 1)]


def num1making(n, count):
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

print(save_re[N])

```

다이나믹 프로그래밍
```python
for i in range(2, N + 1):
    save_re[i] = save_re[i - 1] + 1

    if i % 5 == 0:
        save_re[i] = min(save_re[i], save_re[i // 5] + 1)
    if i % 3 == 0:
        save_re[i] = min(save_re[i], save_re[i // 3] + 1)
    if i % 2 == 0:
        save_re[i] = min(save_re[i], save_re[i // 2] + 1)

print(save_re[N])
```

## 실전2 개미전사

```python
N = int(input())

num_l = list(map(int, input().split()))
re = num_l[1] if num_l[1] > num_l[0] else num_l[0]
sum_n = num_l[0]

for i in range(2, len(num_l)):
    sum_n, re = re, sum_n + num_l[i] if sum_n + num_l[i] > re else re

print(re)
```