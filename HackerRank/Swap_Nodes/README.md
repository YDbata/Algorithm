#Search Swap_Nodes[Algo]

https://www.hackerrank.com/challenges/swap-nodes-algo/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

## 문제 이해

### 규칙

#### Swap operation:

We define depth of a node as follows:

The root node is at depth 1.
If the **depth of the parent node is d**, then **the depth of current node** will be **d+1**.<br>
Given a tree and an integer, **k, in one operation**, we **need to swap** the subtrees of all the nodes at each **depth h**, where **h ∈ [k, 2k, 3k,...]**.<br>
In other words, if h is a multiple of k, swap the left and right subtrees of that level.

You are given a tree of n nodes where nodes are indexed from [1..n] and it is rooted at 1.<br>
You have to perform **t swap operations on it**, and after **each swap operation print the in-order traversal of the current state** of the tree.

#### Function Description

Complete the swapNodes function in the editor below.<br>
It should return a two-dimensional array where each element is an array of integers representing the node indices of an in-order traversal after a swap operation.

swapNodes has the following parameter(s):
- indexes: an array of integers representing **index values of each _node[i]_**, beginning with _node[1]_, the first element, as the root.
  <br>(node[1]은 root의 요소..?아마 자식노드...)
- queries: an array of integers, each representing **a _k_ value**.

### 입력

The first line contains **n**, **number of nodes in the tree**.

Each of the **next n lines** contains two integers, **a b**, <br>where **a** is the index of **left child**, and **b** is the index of **right child** of **ith node**.

#### Note:
**-1** is used to represent **a null node**.<br>
The next line contains an integer, **t, the size of _queries_**.<br>
**Each of the next t lines** contains an integer **_queries[i]_**, each being a value **_k_**.

**Constraints**<br>
- 1<= _n_ <= 1024
- 1<= _t_ <= 100
- 1<= _k_ <= n
- Either a=-1 or 2<=a<=n
- Either b=-1 or 2<=b<=n
- The index of a non-null child will always be greater than that of its parent.

### 출력

For each k, perform the swap operation and **store the indices of your in-order traversal** to your result array.<br>
After all swap operations have been performed, return your result array for printing.

## Input 예시

5<br>
2 3<br>
-1 4<br>
-1 5<br>
-1 -1<br>
-1 -1<br>
1<br>
2<br>

### output
4 2 1 5 3

예시 설명은 hackerrank에 있습니다.

## 풀이

```python
import os
import random
import re
import sys
sys.setrecursionlimit(100000)
```

que에 자식 노드들을 넣어주는 함수 맨앞의 요소를 없애야 할때가 있고 아닐 때가 있다.
```python
def add_n(que, idx, f, start):
    if f:
        t = que[start] - 1
        start += 1
    else:
        t = que.pop(start) - 1
    # print("t", t)
    if idx[t][0] != -1:
        que.append(idx[t][0])
    if idx[t][1] != -1:
        que.append(idx[t][1])
    return start
```

중위순회 print대신 append를 사용 값을 저장하였다.
```python
def inorder(idx, dep, order):
    if idx[dep][0] != -1:
        inorder(idx, idx[dep][0] - 1, order)
    order.append(dep + 1)
    if idx[dep][1] != -1:
        inorder(idx, idx[dep][1] - 1, order)

    return order
```

## main 함수

Node들을 Swap하고 받아온 order리스트를 print하는 사실상 main 함수
```python
def swapNodes(indexes, queries):
    re = []
    for q in queries:
        que = [1]
        start = 0
        for i in range(len(indexes)):
            if (i + 1) % q == 0:
                f = 1
            else:
                f = 0
            num = len(que[start:])
            for i in range(num):
                start = add_n(que, indexes, f, start)
            # print(que, start)
            if start == len(que):
                break

        for i in que:
            tmp = indexes[i - 1][0]
            indexes[i - 1][0] = indexes[i - 1][1]
            indexes[i - 1][1] = tmp

        # print(indexes)
        re.append(inorder(indexes, 0, []))
    return re
```