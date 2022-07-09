n = int(input())

lst = list(map(int, input().split()))
memo = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if lst[i] < lst[j]:
            memo[i] = max(memo[i], memo[j] + 1)

print(n - max(memo))
