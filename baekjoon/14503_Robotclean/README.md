#14503 로봇청소기

## 문제 이해

### 규칙

1. 현재 위치를 청소한다.
2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색한다.
    * 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    * 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    * 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    * 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
    
로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.

### 입력

- 첫째 줄에 **세로 크기 N과 가로 크기 M**이 주어진다. (3 ≤ N, M ≤ 50)
- 둘째 줄에 로봇 **청소기가 있는 칸의 좌표 (r, c)**와 **바라보는 방향 d**가 주어진다.<br>
**d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽**을 바라보고 있는 것이다.
- 셋째 줄부터 N개의 줄에 장소의 상태가 **북쪽부터 남쪽 순서**대로, 각 줄은 **서쪽부터 동쪽 순서**대로 주어진다.<br> **빈 칸은 0, 벽은 1**로 주어진다. 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다.
- **로봇 청소기가 있는 칸의 상태는 항상 빈 칸이다.**

### 출력

로봇 청소기가 **청소하는 칸의 개수를 출력**

## Input 예시

4 4<br>
2 2 3<br>
1 1 1 1<br>
1 0 0 1<br>
1 0 0 1<br>
1 1 1 1<br>

<img src="https://user-images.githubusercontent.com/51112432/126332089-422aaf14-daf3-4695-acf0-5cb147d0a84f.png" width=170 height=300 /><img src="https://user-images.githubusercontent.com/51112432/126331266-62631976-b7f9-48e4-8981-8939ae6a7773.png" width=300 height=300 />
<img src="https://user-images.githubusercontent.com/51112432/126331477-4b4d0668-951e-4b1e-b083-0064b18a507c.png" width=300 height=300 /><br>
처음에는 칠하지 않고 방향을 바꿔서 이동하는 걸로 시작 이 후 청소기가 도착한 곳은 모두 0대신 2로 채우면서 진행하였다.<br>그림의 숫자는 청소 순서이다.

<img src="https://user-images.githubusercontent.com/51112432/126331651-0591324e-2b3b-4e91-8cd5-d01caece08e8.png" width=300 height=300 /><img src="https://user-images.githubusercontent.com/51112432/126332145-2829e361-3229-4d73-b6c4-1c62c267354b.png" width=300 height=300 />

## input 입력 및 함수

```python
n,m = map(int, input().split())

r, c, d = map(int , input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dr = ((-1, 0),(0, 1),(1,0),(0,-1)) # 북, 동, 남, 서
board[r][c] = 2 # 0 청소전 1 벽 2 청소후
result = 1
```

청소기가 board안에 있는지 확인하는 함수
```python
def is_save(x, y):
    try:
        if board[x][y] != 1:
            pass
        return 1
    except:
        return 0
```

청소기가 주변 모든 방향이 청소 후 or 벽일 때까지 실행
```python
def move(r, c, d):
    global result

    count = 0
    while count != 4:
        d -= 1
        if d == -1:
            d = 3

        if is_save(r + dr[d][0], c + dr[d][1]):
            if board[r + dr[d][0]][c + dr[d][1]] == 0:
                r, c = r + dr[d][0], c + dr[d][1]
                board[r][c] = 2
                count = 0
                # d += 1
                result += 1
            else:
                count += 1

    return r, c, d
```

## main

청소기가 move루 후진을 할 수 있으면 후진을 하고 다시 move 아니라면 그대로 작동을 멈춘다.
```python
while True:
    r,c,d = move(r,c,d)
    if board[r - dr[d][0]][c - dr[d][1]] != 1:
        r, c = r - dr[d][0], c - dr[d][1]
        # n, m, d = move(n,m,d)
    else:
        break

print(result)
```
