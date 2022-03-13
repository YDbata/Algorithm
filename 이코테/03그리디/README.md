# 그리디
다른 말로 **'탐욕법'** 이라고 불림

그리디는 보통 코테에서 **창의력**을 요구한다.<br>
이는 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 보는 것이다.

그리디 알고리즘은 기준에 따라 좋은 것을 선택하는 알고리즘이므로<br>
문제에서 '가장 큰 순서대로', '가장 작은 순서대로' 와 같은 기준을 알게 모르게 제시한다.

위에서 제시한 기준은 대부분 정렬을 사용하여 판단할 수 있으며 때문에<br>
'그리디', '정렬' 은 함께 출제되는 경우가 많다.

## 예제3-1 거스름돈
당신은 음식점의 계산을 도와주는 점원이다.<br>
카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이
무한히 존재한다고 가정한다. 손님에게 거슬러 줘야 할 돈이 N원일 때
거슬러 줘야 할 동전의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

### 해답
```python
N = int(input())

count_l = [500, 100, 50, 10]
re = 0
for c in count_l:
    count = N // c
    N -= c * count
    re += count

print(re)
```

### 문제 해설
이 문제의 아이디어는 **'가장 큰 화폐 단위부터'** 돈을 거슬러 주는 것이다.<br>
N원을 거슬러 줘야할 때 500원으로 줄 수 있는 만큼 준뒤에 100원, 50원, 10원 순으로<br>
거슬러주는 것이다.

### 예시
N = 1260<br>
500*2 + 100*2 + 50*1 + 10*1 = 1260<br>
즉, 동전은 6개필요하다.

## 그리디 알고리즘의 정당성
그리디를 실제 문제에 적용하려고 하였을 때, '최적의 해'를 찾을 수 없는 문제가 더 많을 수 있다.<br>
하지만 위에 '거스름돈' 문제와 같이 **정확한 답을 찾을 수 있다는 보장**이 있으면<br>
매우 효과적이고 직관적인 방법이다.

그리디 알고리즘을 사용할 때 주의점은 생각한 아이디어(해법)이 정당한지 검토하여야한다.<br>
대부분의 그리디 알고리즘 문제에서는 아이디어에 대한 정당성을 검토할 수 있어야 답을 도출할 수 있다.

위의 '거스름돈' 은 동전의 단위가 서로 배수의 형태였기에 그리디가 가능했다.<br>
하지만 무작위로 동전이 주어질 경우그리디로 해결할 수 없다.

## 실전문제

### 큰 수의 법칙

#### 스피드 런
```python
N, M, K = map(int, input().split())

num_l = list(map(int, input().split()))
count = 0
re = 0
num_l.sort(reverse=True)

for i in range(M):
    if count == K:
        re += num_l[1]
        count = 0
    else:
        re += num_l[0]
        count += 1

print(re)
```

#### 수학적으로 풀 때
수학적인 연산을 집어넣어 코딩 연산량을 줄인 경우
```python
N, M, K = map(int, input().split())

num_l = list(map(int, input().split()))
count = M//K
re = 0

num_l.sort(reverse=True)

re += count*num_l[1] + (M - count)*num_l[0]

print(re)
```

### 숫자 카드 게임

#### 스피드런
```python
N, M = map(int, input().split())

min_l = []
for c in range(N):
    min_l.append(min(list(map(int, input().split()))))

print(max(min_l))
```

#### 메모리를 신경 쓴 버전
리스트를 사용하지 않고 해결하면서 공간 확보
```python
N, M = map(int, input().split())
min_n = 0
re = 0
for c in range(N):
    min_n = min(list(map(int, input().split())))
    re = max(re, min_n) 

print(re)
```

### 1이 될 때까지
#### 스피드런
```python
N, K = map(int, input().split())
re = 0
while N != 1:
    if N % K == 0:
        N //= K
    else:
        N -= 1
    re += 1

print(re)
```

#### 시간복잡도를 생각한 답
N이 K보다 작아지면 멈추고 N - 1을 re에 더하면서 1을 빼는 연산을 줄임
```python
N, K = map(int, input().split())
re = 0
while N >= K:
    if N % K == 0:
        N //= K
    else:
        N -= 1
    re += 1

re += N - 1

print(re)
```