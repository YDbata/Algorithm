N = int(input())

count_l = [500, 100, 50, 10]
re = 0
for c in count_l:
    count = (N // c)
    N -= c * count
    re += count

print(re)
