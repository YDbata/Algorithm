t = int(input())

for _ in range(t):
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    memo = [[-1 for _ in range(n)] for _ in range(n)]
    memo[0][0] = board[0][0]

