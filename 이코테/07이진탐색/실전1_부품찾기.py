N = int(input())

n_l = list(map(int, input().split()))
M = int(input())
m_l = list(map(int, input().split()))

for i in m_l:
    if i in n_l:
        print("yes", end=" ")
    else:
        print("no", end=" ")

