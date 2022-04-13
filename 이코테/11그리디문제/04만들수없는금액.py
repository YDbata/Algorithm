n = int(input())

money = list(map(int, input().split()))

money.sort(reverse=True)


def make_num(num, m, s, n):
    if num == 0:
        return 1
    if s < n:
        if num < m[s]:
            return make_num(num, m, s + 1, n)
        else:
            return make_num(num - m[s], m, s + 1, n)
    else:
        return 0


for i in range(1, sum(money) + 1):
    if make_num(i, money, 0, n) == 0:
        print(i)
        break
