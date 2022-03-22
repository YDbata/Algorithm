# 정렬

'정렬'이란 데이터를 특정한 기준에 따라서 순서대로 나열한 것이다.

정렬은 프로그램을 작성할 때 가장 많이 사용되는 알고리즘 중에 하나이다.<br>
이 책에서는 코딩테스트의 합격이 목적이므로 '선택정렬, 삽입정렬, 퀵 정렬, 계수 정렬'들만 언급한다.<br>
이와 함께 파이썬에서 사용되는 기본 정렬 라이브러리를 적용하여 좀 더 효과적인 정렬 수행법도 함께 본다.

정렬은 상황에 적절하지 못한 정렬 알고리즘을 이용하면 장연히 프로그램은 비효울적으로 동작하고 시간이 많이 소요된다.<br>
때문에 정렬 알고리즘을 공부하다보면 자연스럽게 알고리즘 효울의 중요성을 깨닫는다.

## 선택정렬

데이터 중 가장 작은 원소를 선택하여 맨 앞의 원소와 바꾸고<br>
그다음 작은 데이터를 선택해 앞에서 두번째 데이터와 바꾸는 과정으로 이루어져있다.

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def swap(x, y):
    array[x], array[y] = array[y], array[x]
    # tmp = array[x]f
    # array[x] = array[y]
    # array[y] = tmp


for i in range(len(array)):
    min_idx = i
    for n in range(i + 1, len(array)):
        if array[min_idx] > array[n]:
            min_idx = n

    if min_idx != i:
        swap(min_idx, i)

print(*array, sep=" ")
```

### 선택정렬의 시간복잡도
선택정렬의 시간복잡도는 이중 for문이 가장 큰 연산을 담당하므로 빅오표기법으로 나타내면
최선과 최악의 경우 모두 O(N²)이다.

## 삽입정렬

한 데이터를 확인하여 적절한 위치에 삽입한다고 하여 삽입정렬이다.

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j-1] = array[j - 1], array[j]
        else:
            break

print(*array, sep=" ")
```

## 퀵 정렬

```python

```