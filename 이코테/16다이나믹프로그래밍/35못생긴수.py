n = int(input())
lst = [1]
i = 0

while len(lst) <= n:
    if lst[i]*2 not in lst:
        lst.append(lst[i]*2)
    if lst[i] * 3 not in lst:
        lst.append(lst[i] * 3)
    if lst[i] * 5 not in lst:
        lst.append(lst[i] * 5)

    lst.sort()
    i += 1


print(lst[n - 1])