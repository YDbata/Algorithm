def solution(N, stages):
    answer = [i for i in range(1, N + 1)]
    num = [0 for i in range(N + 1)]

    for s in stages:
        num[s - 1] += 1
    num2 = [len(stages)]
    for n in range(N):
        num2.append(num2[n] - num[n])

    def func(x):
        if num2[x - 1] == 0:
            return 0
        return num[x - 1] / num2[x - 1]

    new_answer = sorted(answer, key=func, reverse=True)
    return new_answer