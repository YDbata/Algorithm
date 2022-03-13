# 스피드런

'''N, K = map(int, input().split())
re = 0
while N != 1:
    if N % K == 0:
        N //= K
    else:
        N -= 1
    re += 1

print(re)'''

# 시간복잡도를 생각한 답

N, K = map(int, input().split())
re = 0
while N >= K:
    if N % K == 0:
        N //= K
    else:
        N -= 1
    re += 1

re += N - 1

print(re)
