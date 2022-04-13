n = int(input())

l = list(map(int, input().split()))

l.sort(reverse=True)

count = 0
re = 0

while count < n:
    count += l[count]
    re += 1

if count == n:
    print(re)
else:
    print(re - 1)