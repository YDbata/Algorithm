# 최단경로
**'최단경로'**란 가장 짧은 경로를 찾는 알고리즘이다.<br>
최단경로 문제는 보통 그래프를 이용해서 표현한다.<br>
각 지점을 **'노드'**, 노드를 연결하는 도로는 **'간선'** 이라고 한다.

컴퓨터 공학 학부수주넹서 사용하는 최단 거리 알고리즘은 다익스트라, 플로이드 워셜, 벨만 포드 정도이다.<br>
다익스트라와 플로이드 워셜이 코딩테스트에서 가장 많이 출제 되므로 이책에서는 이 두가지만 다룬다.< br>
이번장은 그리디와 이어지는 면이 있다. 즉, 그리디와 다이나믹프로그래밍의 한 유형으로 볼 수 있다.

## 다익스트라
'다익스트라' 는 

## 실전1 미래도시

```python
N, M = map(int, input().split())
edge = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    edge[s][e] = 1
    edge[e][s] = 1

x, k = map(int, input().split())


def road(s, e):
    q = []
    for i in range(1, N + 1):
        if edge[s][i] == 1:
            if i == e:
                return 1
            else:
                q.append([s, i, 1])

    while q and s != q[0][1]:
        for i in range(1, N + 1):
            if edge[q[0][1]][i] == 1:
                if i != e and q[0][0] != i:
                    q.append([q[0][1], i, q[0][2] + 1])
                elif i == e:
                    return q[0][2] + 1

        del q[0]

    return -1


kr = road(1, k)
xr = road(k, x)
if kr > 0 and xr > 0:
    print(kr + xr)
else:
    print(-1)

```
## 전보

```python
N, M = map(int, input().split())
edge = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    edge[s][e] = 1
    edge[e][s] = 1

x, k = map(int, input().split())


def road(s, e):
    q = []
    for i in range(1, N + 1):
        if edge[s][i] == 1:
            if i == e:
                return 1
            else:
                q.append([s, i, 1])

    while q and s != q[0][1]:
        for i in range(1, N + 1):
            if edge[q[0][1]][i] == 1:
                if i != e and q[0][0] != i:
                    q.append([q[0][1], i, q[0][2] + 1])
                elif i == e:
                    return q[0][2] + 1

        del q[0]

    return -1


kr = road(1, k)
xr = road(k, x)
if kr > 0 and xr > 0:
    print(kr + xr)
else:
    print(-1)

```