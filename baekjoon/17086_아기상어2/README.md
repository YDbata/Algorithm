#17086 아기상어2

https://www.acmicpc.net/problem/17086

## 문제 이해

### 규칙

N×M 크기의 공간에 아기 상어 여러 마리가 있다.<br>
공간은 1×1 크기의 정사각형 칸으로 나누어져 있다.<br>
한 칸에는 아기 상어가 최대 1마리 존재한다.

어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다.<br>
두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 이동은 인접한 8방향(대각선 포함)이 가능하다.

안전 거리가 가장 큰 칸을 구해보자.

#### 규칙 시각화

검은색이 아기상어, 빨간색이 안전거리

<img src="https://user-images.githubusercontent.com/51112432/130468924-cb83b8d6-ce72-4173-8648-48a64aaa6423.png" width="300">

### 입력

첫째 줄에 **공간의 크기** **N과 M(2 ≤ N, M ≤ 50)**이 주어진다.<br>
둘째 줄부터 **N개의 줄에 공간의 상태**가 주어지며, **0은 빈 칸, 1은 아기 상어**가 있는 칸이다.<br>
빈 칸의 개수가 한 개 이상인 입력만 주어진다.

### 출력

첫째 줄에 **안전 거리의 최댓값**을 출력한다.

## Input 예시
### 1번
5 2<br>
0 2 0 1 0<br>
1 0 1 0 0<br>
0 0 0 0 0<br>
2 0 0 1 1<br>
2 2 0 1 2<br>

정답: 10

### 2번
7 4<br>
0 0 0 1<br>
0 1 0 0<br>
0 0 0 0<br>
0 0 0 1<br>
0 0 0 0<br>
0 1 0 0<br>
0 0 0 1<br>

정답: 2

## 풀이

BFS로 풀어도 좋았겠지만 범위 자체가 2500까지 밖에 안되어서 중복처리를 따로 해주는것보다 반복으로 풀어내는 것이 빠르다고 판단 하였다.

처음에 abs를 안해서 틀렸었다.

```python
n, m = map(int, input().split())

maps = []
shark = []
re = 0
for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(m):
        if maps[i][j]:
            shark.append((i, j))

for x in range(n):
    for y in range(m):
        if maps[x][y] == 0:
            tmp = 2500
            for s in shark:
                xt = abs(x - s[0])
                yt = abs(y - s[1])
                if xt > yt:
                    if tmp > xt:
                        tmp = xt
                else:
                    if tmp > yt:
                        tmp = yt

            if tmp > re:
                re = tmp

print(re)
```
