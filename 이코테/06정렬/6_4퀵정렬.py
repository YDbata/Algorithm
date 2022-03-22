array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

'''def quick(left, right):
    if left + 1 >= right:
        if array[left] > array[right]:
            array[left], array[right] = array[right], array[left]
        return

    t_l = left
    t_r = right
    left += 1
    while left < right:
        if array[left] > array[t_l]:
            if array[right] < array[t_l]:
                array[left], array[right] = array[right], array[left]
                left += 1
            right -= 1
        elif array[right] < array[t_l]:
            left += 1
        else:
            left += 1
            right -= 1

    if array[left] < array[t_l]:
        array[left], array[t_l] = array[t_l], array[left]
    else:
        array[left - 1], array[t_l] = array[t_l], array[left - 1]

    quick(t_l, left - 1)
    quick(left, t_r)

    return


quick(0, len(array) - 1)

print(*array, sep=" ")'''


# noti: 개선버전

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
