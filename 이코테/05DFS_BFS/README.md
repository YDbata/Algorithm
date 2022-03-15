# DFS/BFS

'탐색'이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정이다.

## 실전 문제

### 음료수 얼려먹기

```python
N, M = map(int, input().split())
board = []


def is_save(numx, numy):
    return 1 if -1 < numx < N and -1 < numy < M else 0


def fill(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    board[x][y] = 1
    for i in range(4):
        if is_save(x + dx[i], y + dy[i]):
            if board[x + dx[i]][y + dy[i]] == 0:
                fill(x + dx[i], y + dy[i])


for n in range(N):
    board.append(list(map(int, list(input()))))

count = 0
for n in range(N):
    for m in range(M):
        if board[n][m] == 0:
            fill(n, m)
            count += 1
print(count)

```
### 미로 탈출
```python
N, M = map(int, input().split())

board = []
re = 40000


def is_save(x, y):
    return 1 if -1 < x < N and -1 < y < M else 0


def find(x, y, count):
    global re

    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    if (x, y) == (N - 1, M - 1):
        re = min(re, count)
        return 0

    for i in range(4):
        if is_save(x + dx[i], y + dy[i]) and board[x + dx[i]][y + dy[i]] == 1:
            board[x][y] = 2
            find(x + dx[i], y + dy[i], count + 1)
            board[x][y] = 1

    return 0


for n in range(N):
    board.append(list(map(int, list(input()))))

find(0, 0, 0)

print(re + 1)

```
