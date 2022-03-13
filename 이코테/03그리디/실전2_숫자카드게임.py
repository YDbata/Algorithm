# 스피드런
'''N, M = map(int, input().split())

min_l = []
for c in range(N):
    min_l.append(min(list(map(int, input().split()))))

print(max(min_l))'''

# 메모리를 신경 쓴 버전

N, M = map(int, input().split())
min_n = 0
re = 0
for c in range(N):
    min_n = min(list(map(int, input().split())))
    re = max(re, min_n)

print(re)
