N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

re = 0
for i in range(K):
    re += A[i] if A[i] > B[i] else B[i]

print(sum(A[K:], re))
