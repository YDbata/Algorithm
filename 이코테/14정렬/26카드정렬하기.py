import heapq

n = int(input())
num_l = []
for i in range(n):
    heapq.heappush(num_l, int(input()))
re = 0
for i in range(n - 1):
    tmp = heapq.heappop(num_l) + heapq.heappop(num_l)
    heapq.heappush(num_l, tmp)
    re += tmp

print(re)
