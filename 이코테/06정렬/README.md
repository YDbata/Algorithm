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
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick(left, right):
    if left + 1 >= right:
        if array[left] > array[right]:
            array[left], array[right] = array[right], array[left]
        return

    t_l = left
    t_r = right
    left += 1
    while left < right:
        if array[left] > array[t_l]:
            if array[right] < array[t_l]:
                array[left], array[right] = array[right], array[left]
                left += 1
            right -= 1
        elif array[right] < array[t_l]:
            left += 1
        else:
            left += 1
            right -= 1

    if array[left] < array[t_l]:
        array[left], array[t_l] = array[t_l], array[left]
    else:
        array[left - 1], array[t_l] = array[t_l], array[left - 1]

    quick(t_l, left - 1)
    quick(left, t_r)

    return


quick(0, len(array) - 1)

print(*array, sep=" ")

# noti: 개선버전

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
```


## 실전문제

### 위에서 아래로

```python
N = int(input())

l = []
for _ in range(N):
    l.append(int(input()))
l.sort(reverse=True)
print(*l, sep=" ")
```

### 성적이 낮은 순서로 학생 출력하기

```python
N = int(input())

l2 = []
for _ in range(N):
    tmp = input().split()
    l2.append([tmp[0], int(tmp[1])])

l2.sort(key=lambda x : x[1])

print(*list(zip(*l2))[0], sep=" ")

```

### 두 배열의 원소 교체
```python
N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

re = 0
for i in range(K):
    re += A[i] if A[i] > B[i] else B[i]

print(sum(A[K:], re))

```