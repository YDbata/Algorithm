N = int(input())

l = []
for _ in range(N):
    l.append(int(input()))
l.sort(reverse=True)

print(*l, sep=" ")
