def maxh_insert(an, n, oper):
    max_heap.append(int(oper[1]))
    if max_heap[n] ^ 1:
        while n != 0 and max_heap[n] > max_heap[(n - 1) // 2]:
            tmp = max_heap[n]
            max_heap[n] = max_heap[(n - 1) // 2]
            max_heap[(n - 1) // 2] = tmp
            n = (n - 1) // 2
    else:
        while n != 0 and max_heap[n] > max_heap[(n // 2) - 1]:
            tmp = max_heap[n]
            max_heap[n] = max_heap[(n // 2) - 1]
            max_heap[(n // 2) - 1] = max_heap[n]
            n = (n // 2) - 1
    an[0] = max_heap[0]
    return 0


def minh_insert(an, n, oper):
    min_heap.append(int(oper[1]))
    if min_heap[n] ^ 1:
        while n != 0 and min_heap[n] < min_heap[(n - 1) // 2]:
            tmp = min_heap[n]
            min_heap[n] = min_heap[(n - 1) // 2]
            min_heap[(n - 1) // 2] = tmp
            n = (n - 1) // 2
    else:
        while n != 0 and min_heap[n] < min_heap[(n // 2) - 1]:
            tmp = min_heap[n]
            min_heap[n] = min_heap[(n // 2) - 1]
            min_heap[(n // 2) - 1] = min_heap[n]
            n = (n // 2) - 1

    an[1] = min_heap[0]
    return 0


def max_del(an, n):
    global max_heap, min_heap
    if n == 0:
        max_heap = []
        min_heap = []
    else:
        m = max_heap[0]
        lm = len(max_heap)

        count = 0
        while lm > count * 2 + 1:
            if lm >= (count + 1) * 2 + 1 and max_heap[count * 2 + 1] < max_heap[(count + 1) * 2]:
                max_heap[count] = max_heap[(count + 1) * 2]
                count = (count + 1) * 2
            else:
                max_heap[count] = max_heap[count * 2 + 1]
                count = count * 2 + 1

        del max_heap[count]

        count = min_heap.index(m)
        while lm > count * 2 + 1:
            if lm >= (count + 1) * 2 + 1 and min_heap[count * 2 + 1] < min_heap[(count + 1) * 2]:
                min_heap[count] = min_heap[(count + 1) * 2]
                count = (count + 1) * 2
            else:
                min_heap[count] = min_heap[count * 2 + 1]
                count = count * 2 + 1

        del min_heap[count]

    if max_heap:
        an[0] = max_heap[0]
        an[1] = min_heap[0]
    else:
        an[0] = 0
        an[1] = 0
    return 0


def min_del(an, n):
    global min_heap, max_heap
    # 최소값 삭제
    if n == 0:
        max_heap = []
        min_heap = []
    else:
        m = min_heap[0]
        lm = len(max_heap)

        count = 0
        while lm > count * 2 + 1:
            if lm >= (count + 1) * 2 + 1 and min_heap[count * 2 + 1] > min_heap[(count + 1) * 2]:
                min_heap[count] = min_heap[(count + 1) * 2]
                count = (count + 1) * 2
            else:
                min_heap[count] = min_heap[count * 2 + 1]
                count = count * 2 + 1

        del min_heap[count]

        count = max_heap.index(m)
        while lm > count * 2 + 1:
            if lm >= (count + 1) * 2 + 1 and max_heap[count * 2 + 1] < max_heap[(count + 1) * 2]:
                max_heap[count] = max_heap[(count + 1) * 2]
                count = (count + 1) * 2
            else:
                max_heap[count] = max_heap[count * 2 + 1]
                count = count * 2 + 1

        del max_heap[count]

    if min_heap:
        an[0] = max_heap[0]
        an[1] = min_heap[0]
    else:
        an[0] = 0
        an[1] = 0

    return 0


max_heap = []
min_heap = []


def solution(operations):
    # def solution():
    answer = [0, 0]
    # operations = input().split(',')
    # operations = operations[1:-1].split(',')
    count = 0
    for oper in operations:
        print(max_heap, min_heap, oper, answer)
        oper = oper.split()
        if oper[0] == "D" and max_heap:
            # 삭제
            count -= 1
            # print(count)
            if oper[1] == "1":
                max_del(answer, count)
            else:
                min_del(answer, count)

        elif oper[0] == "I":
            # 삽입
            maxh_insert(answer, count, oper)
            minh_insert(answer, count, oper)

            count += 1

    # print(answer)
    return answer

solution()
