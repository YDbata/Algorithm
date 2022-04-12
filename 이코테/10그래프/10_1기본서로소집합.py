def find_parent(parent, x):
    if parent[x] != x:
        # 경로 압축 기법으로 시간복잡도 개선가능
        # return find_parent(parent, parent[x])
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:  # 더 작은 수를 부모 노드로 만들기
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i
# 10-4 싸이클발생 확인
cycle = False

for i in range(e):
    a, b = map(int, input().split())
    # 10-4싸이클 여부확인
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    union_parent(parent, a, b)

print('싸이클 여부', cycle)
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')
print()

print('부모 테이블: ', end='')
print(*parent[1:], sep=" ")

'''10-1~2예제
6 4
1 4
2 3
2 4
5 6
각 원소가 속한 집합: 1 1 1 1 5 5 
부모 테이블: 1 1 2 1 5 5

10-4
싸이클 예제
3 3
1 2
1 3
2 3
싸이클 여부 True
각 원소가 속한 집합: 1 1 1 
부모 테이블: 1 1 1
'''
