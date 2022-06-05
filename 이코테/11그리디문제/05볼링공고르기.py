from itertools import combinations

n, m = map(int, input().split())

m_l = [0 for _ in range(m + 1)]

for num in list(map(int, input().split())):
    m_l[num] += 1

re = 0
for c in combinations(m_l, 2):
    re += c[0]*c[1]
print(re)
