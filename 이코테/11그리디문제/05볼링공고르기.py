n, m = map(int, input().split())

m_l = [n for _ in range(m + 1)]

for num in list(map(int, input().split())):
    m_l[num] -= 1

re = 0
for i in range(1, m + 1):
    re += n - m_l[i]

print(sum(m_l[1:]))
