N, M = map(int, input().split())


def find_team(parent, x):
    if parent[x] != x:
        parent[x] = find_team(parent, parent[x])
    return parent[x]


student_l = [i for i in range(N + 1)]

for _ in range(M):
    cate, a, b = map(int, input().split())
    if cate:
        # 확인연산
        if find_team(student_l, a) == find_team(student_l, b):
            print("YES")
        else:
            print("NO")
    else:
        # 합치기 연산
        if find_team(student_l, a) < find_team(student_l, b):
            student_l[b] = a
        else:
            student_l[a] = b

'''
실전1 예제
7 8
0 1 3
1 1 7
NO
0 7 6
1 7 1
NO
0 3 7
0 4 2
0 1 1 
1 1 1
YES

'''
