N = int(input())

l2 = []
for _ in range(N):
    tmp = input().split()
    l2.append([tmp[0], int(tmp[1])])

l2.sort(key=lambda x : x[1])

print(*list(zip(*l2))[0], sep=" ")
