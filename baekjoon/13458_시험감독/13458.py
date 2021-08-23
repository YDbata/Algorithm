n = int(input())
a_list = list(map(int, input().split()))
b, c = map(int, input().split())

count = 0

for a in a_list:
    count += 1
    if a - b > 0:
        a -= b
        if a%c:
            count += a//c + 1
        else:
            count += a//c

print(count)