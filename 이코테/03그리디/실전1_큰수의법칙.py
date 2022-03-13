# title: 큰수의 법칙
# 스피드런
'''N, M, K = map(int, input().split())

num_l = list(map(int, input().split()))
count = 0
re = 0
num_l.sort(reverse=True)

for i in range(M):
    if count == K:
        re += num_l[1]
        count = 0
    else:
        re += num_l[0]
        count += 1

print(re)'''

# python 식
N, M, K = map(int, input().split())

num_l = list(map(int, input().split()))
count = M//K
re = 0

num_l.sort(reverse=True)

re += count*num_l[1] + (M - count)*num_l[0]

print(re)
