from sys import stdin
from itertools import combinations as comb
r = stdin.readline

n,m = map(int, r().strip().split())
city = [r().strip().split() for i in range(n)]
ans = 1e9
houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if city[i][j] == '1':
            houses.append((i,j))
        elif city[i][j] == '2':
            chickens.append((i,j))

dists = [list(map(lambda x : abs(x[0]-c[0]) + abs(x[1]-c[1]), houses)) for c in chickens]
for co in comb((i for i in range(len(chickens))), m):
    res = sum(map(min, zip(*[dists[i] for i in co])))


    if res < ans:
        ans = res
print(ans)