array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def swap(x, y):
    tmp = array[x]
    array[x] = array[y]
    array[y] = tmp


for i in range(len(array)):
    min_idx = i
    for n in range(i + 1, len(array)):
        if array[min_idx] > array[n]:
            min_idx = n

    if min_idx != i:
        swap(min_idx, i)

print(*array, sep=" ")
