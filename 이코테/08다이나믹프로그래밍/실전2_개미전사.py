N = int(input())

num_l = list(map(int, input().split()))
re = num_l[1] if num_l[1] > num_l[0] else num_l[0]
sum_n = num_l[0]

for i in range(2, len(num_l)):
    sum_n, re = re, sum_n + num_l[i] if sum_n + num_l[i] > re else re

print(re)
