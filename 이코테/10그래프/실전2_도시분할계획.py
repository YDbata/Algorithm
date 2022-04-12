import sys

N, M = map(int, input().split())

cost_l = []
nodes = [i for i in range(N + 1)]
re = 0
max_edge = 0

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    cost_l.append((a, b, c))

cost_l.sort(key=lambda x: x[2])


def find_house(parent, x):
    if parent[x] != x:
        parent[x] = find_house(parent, parent[x])
    return parent[x]


def union_house(parent, a, b):
    a = find_house(parent, a)
    b = find_house(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for c in cost_l:
    if find_house(nodes, c[0]) != find_house(nodes, c[1]):
        union_house(nodes, c[0], c[1])
        max_edge = c[2]
        re += c[2]

print(re - max_edge)
