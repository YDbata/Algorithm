n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

location = list(map(int, input().split()))
rootlist = [i for i in range(n + 1)]

