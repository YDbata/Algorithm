N, M = map(int, input().split())

len_l = list(map(int, input().split()))

min_n = 0
m_n = min(len_l)
max_n = max(len_l)
sum_n = 0
for i in len_l:
    if i > m_n:
        sum_n += i - m_n

while min_n != max_n:
    m = (max_n + m_n)//2
    if sum_n > M:
        sum_n = 0
        for i in len_l:
            if i > m:
                sum_n += i - m
        min_n, m_n = m_n, m

    elif sum_n < M:
        sum_n = 0
        for i in len_l:
            if i > m_n//2:
                sum_n += i - m_n//2
        max_n, m_n = m_n, m_n//2
    else:
        break

print(m_n)
