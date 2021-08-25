#1260 DFS와 BFS

https://www.acmicpc.net/problem/1260

## 문제 이해

### 규칙

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.<br>
단, 방문할 수 있는 정점이 여러 개인 경우에는 **정점 번호가 작은 것**을 먼저 방문하고,<br>
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 **1번부터 N번**까지이다.

### 입력

첫째 줄에 **정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V**가 주어진다.<br>
다음 M개의 줄에는 간선이 연결하는 **두 정점의 번호**가 주어진다.<br>
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 **양방향**이다.

### 출력

첫째 줄에 **DFS를 수행**한 결과를, 그 다음 줄에는 **BFS를 수행**한 결과를 출력한다.<br>
**V부터 방문된 점**을 순서대로 출력하면 된다.

## Input 예시
### 1번

4 5 1<br>
1 2<br>
1 3<br>
1 4<br>
2 4<br>
3 4<br>

정답:<br>
1 2 4 3<br>
1 2 3 4

### 2번

5 5 3<br>
5 4<br>
5 2<br>
1 2<br>
3 4<br>
3 1

정답:<br>
3 1 2 5 4<br>
3 1 4 2 5

## 풀이

Linked List로 풀려다가 작은 수부터 탐색이라는 조건에 맞지 않아 포기했다.<br>
작은 수 부터 탐색하려면 값을 모두 집어넣고 sort를 해야하는데 이렇게하는 것이 시간이 더 오래 걸릴것같았다. ~~아닐려나...~~<br>
때문에 2차원 배열을 만들어서 사용하였다.

```python

def dfs(node):
    for nd in range(1, n + 1):
        if visit[nd] == 0 and node_list[node][nd] == 1:
            print(nd, end=" ")
            visit[nd] = 1
            dfs(nd)

if __name__=="__main__":
    n, m, v = map(int, input().split())

    node_list = [[0 for _ in range(n + 1)] for i in range(n + 1)]
    visit = [0 for i in range(n + 1)]
    bfs_stack = [v]

    for _ in range(m):
        p, s = map(int, input().split())
        node_list[p][s] = 1
        node_list[s][p] = 1

    print(v, end=" ")
    visit[v] = 1
    dfs(v)

    print()
    visit = [0 for i in range(n + 1)]
    while bfs_stack:
        s_node = bfs_stack.pop(0)
        print(s_node, end=" ")
        visit[s_node] = 1
        for y in range(1, n + 1):
            if visit[y] == 0 and node_list[s_node][y] == 1:
                bfs_stack.append(y)
                visit[y] = 1
```
<img src="./img.png" width="400"/>