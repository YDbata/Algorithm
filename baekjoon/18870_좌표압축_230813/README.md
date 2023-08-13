# 18870 좌표 압축

https://www.acmicpc.net/problem/18870

## 문제 이해

x1, x2, x3, ... xn 이 있을 때<br>
임의의 xi를 좌표 압축을 할 때 xi > xj인 xj의 수가 압축된 좌표이다.<br>ㅈ
즉, 다른 x들이 xi보다 작은 경우를 세면 된다.

### 입력

첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

### 출력

첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

## 잘못된 풀이
아래 풀이는 정답은 맞지만 시간이 초과된다.<br>
시간복잡도가 O(n^2)이기 때문이다.
```c
#include <stdio.h>

int xarr[999999];
int re[999999] = { 0, };
int main() {
    int n;
    scanf("%d", &n);
    // scan을 하나 받을 때마다 앞에서 부터 비교하고 압축 적용
    for (int i = 0; i < n; i++) {
        scanf("%d", &xarr[i]);
        for (int j = 0; j < i; j++) {
            if (xarr[j] < xarr[i]) {
                re[i] += 1;
            }
            else if (xarr[j] > xarr[i]) {
                re[j] += 1;
            }
        }
    }

    for (int z = 0; z < n; z++) {
        printf("%d ", re[z]);
    }
    return 0;
}
```

## 맞는 풀이
결국 남의 블로그를 좀 봤다.<br>
먼저 구조체를 선언한다.<br>
이 후 퀵소트로 내림차순 정렬을 하고 압축 좌표를 매긴뒤에 다시 순서별로 정렬을 하여
해결하였다.

그 외에 더 많은 블로그를 찾았지만 아래 풀이가 제일 간단하여 수록한다.

```c
#include<stdio.h>
#include<stdlib.h>

int N;

typedef struct point {
    int x;
    int x_;
    int order;
} POINT;

POINT points[1000020];

int compare(const void* first, const void* second) {
    if (((POINT*)first)->x < ((POINT*)second)->x)
        return -1;
    else if (((POINT*)first)->x > ((POINT*)second)->x)
        return 1;
    else
        return 0;
}

int compare1(const void* first, const void* second) {
    if (((POINT*)first)->order < ((POINT*)second)->order)
        return -1;
    else if (((POINT*)first)->order > ((POINT*)second)->order)
        return 1;
    else
        return 0;
}

int main(void) {

    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%d", &points[i].x);
        points[i].order = i;
    }

    qsort(points, N, sizeof(POINT), compare);

    for (int i = 0; i < N; i++) {

        if (i == 0) {
            points[i].x_ = 0;
        }
        else {
            if (points[i - 1].x == points[i].x) {
                points[i].x_ = points[i - 1].x_;
            }
            else {
                points[i].x_ = points[i - 1].x_+1;
            }
        }
    }

    qsort(points, N, sizeof(POINT), compare1);

    for (int i = 0; i < N; i++) {
        printf("%d ", points[i].x_);
    }
    printf("\n");
}
```
![img.png](19532_c.png)