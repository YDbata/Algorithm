#16234 인구 이동

https://www.acmicpc.net/problem/16234

## 문제 이해

### 규칙

인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

* 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
* 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
* 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
* 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
* 연합을 해체하고, 모든 국경선을 닫는다.

각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.

### 입력

첫째 줄에 **N, L, R**이 주어진다. **(1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)**

둘째 줄부터 **N개의 줄에 각 나라의 인구수**가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)

인구 이동이 발생하는 일수가 **2,000번 보다 작거나 같은 입력**만 주어진다.

### 출력

**인구 이동이 며칠 동안 발생**하는지 첫째 줄에 출력한다.

## Input 예시

2 20 50<br>
50 30<br>
30 40<br>

예시 풀이는 백준에 있습니다.

## 재귀 깊이 제한 해제 및 dx, dy

```python
import sys
sys.setrecursionlimit(1000000)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 좌우상하
```

현재위치가 a배열 안에 있는지 확인하는 함수
```python
def is_save(x1, y1):
    if -1 < x1 < n and -1 < y1 < n:
        return 1
    return 0
```

4방향에 합칠 수 있는 국가를 합치고 합친 국가 기준 다시 dfs를 실행하는 재귀함수
```python
def dfs(x, y):
    global idx, count
    ssum = 0
    for i in range(4):
        if is_save(x + dx[i], y + dy[i]) and (l <= abs(a[x][y] - a[x + dx[i]][y + dy[i]]) <= r):
            if a_idx[x + dx[i]][y + dy[i]] == 0:
                ssum += a[x + dx[i]][y + dy[i]]
                idx.append((x + dx[i], y + dy[i]))
                a_idx[x + dx[i]][y + dy[i]] = 1
                count += 1
                ssum += dfs(x + dx[i], y + dy[i])
    return ssum
```

## main

### 시간초과 해결 IDEA

<img src="https://user-images.githubusercontent.com/51112432/126535784-42cf7d9e-cbb9-4eee-8c22-db95cd1f3f70.png" width="350" height="300"/>

모든 국가위에서 dfs를 실행하지않고 모든 국가를 탐색할 수 있다.
```python
if __name__ == "__main__":
    n, l, r = map(int, input().split())

    a = [list(map(int, input().split())) for i in range(n)]
    re = -1
    while True:
        flag = False
        re += 1
        a_idx = [[0 for i in range(n)] for j in range(n)]
        idx = []

        t = 1
        for ro in range(0, n, 1):
            if t == 0:
                t = 1
            else:
                t = 0

            for c in range(t, n, 2):
                count = 1
                idx = []
                tsum = a[ro][c]
                if a_idx[ro][c] == 0:
                    idx = [(ro, c)]
                    a_idx[ro][c] = 1
                    tsum += dfs(ro, c)

                if tsum > a[ro][c]:
                    flag = True

                for index in idx:
                    a[index[0]][index[1]] = tsum // count

        if not flag:
            break

    print(re)
```