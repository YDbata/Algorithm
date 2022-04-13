

def solution(food_times, k):
    answer = 0
    cl = l = len(food_times)
    length = 0
    food_times_s = list(set(food_times))
    food_times_s.sort()
    count = 0
    tmp = 0

    print(food_times_s, food_times)
    while k > length:
        print(count, k, length)
        length += l * (food_times_s[count] - tmp)
        l -= food_times.count(food_times_s[count])
        tmp = food_times_s[count]
        count += 1

    return cl - (length - k)


print(solution([3,2,1], 6))
