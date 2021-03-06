#2805 나무자르기

https://www.acmicpc.net/problem/2805

## 문제 이해

### 규칙

목재절단기는 다음과 같이 동작한다.<br>
먼저, 상근이는 **절단기에 높이 H**를 지정해야 한다.<br>
높이를 지정하면 **톱날이 땅으로부터 H미터 위**로 올라간다.<br>
그 다음, **한 줄에 연속**해있는 나무를 모두 절단해버린다.<br>
따라서, **높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것**이고, **낮은 나무는 잘리지 않을 것**이다.

**설명 예시**
<br>예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자.<br>
상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다.<br>
(총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.

상근이는 환경에 매우 관심이 많기 때문에, **나무를 필요한 만큼만** 집으로 가져가려고 한다.<br>
이때, **적어도 M미터**의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

### 입력

**첫째 줄**에 **나무의 수 N**과 상근이가 집으로 가져가려고 하는 **나무의 길이 M**이 주어진다.<br>
(1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)

**둘째 줄**에는 **나무의 높이**가 주어진다.<br>
나무의 높이의 합은 **항상 M보다 크거나 같기** 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다.<br>
**높이는 1,000,000,000보다 작거나 같은 양의 정수** 또는 **0**이다.

### 출력

적어도 M미터의 나무를 집에 가져가기 위해서 **절단기에 설정할 수 있는 높이의 최댓값**을 출력한다.

## Input 예시

5 20<br>
4 42 40 26 46

정답 : 36

### 반례 모음

https://joey09.tistory.com/113

## 풀이 

재귀 깊이 제한 해제 및 dx, dy
```python
import math

if __name__ == "__main__":
    n, m = map(int, input().split())

    tree = list(map(int, input().split()))
    tree.append(0)
    tree.sort(reverse=True)
    t_sum = 0 # 상근이가 가져갈 나무 길이
    t_count = 1 # 한번에 잘리는 나무 개수
    re = 0 # 위에서 부터 어느정도 내려와서 절단기를 설정해야하는지
    for i in range(n):
        if t_sum + t_count*(tree[i] - tree[i + 1]) >= m: # 나무길이를 sort하였으므로 i번째가 i+1보다 무조건 같거나 크다.
            re += math.ceil((m - t_sum)/t_count) # 가장큰나무에서 내려온 절단기 높이
            t_sum += math.ceil((m - t_sum)/t_count)*t_count
            break
        else:
            re += (tree[i] - tree[i + 1])
            t_sum += t_count*(tree[i] - tree[i + 1])
        t_count += 1

    print(tree[0] - re)
```