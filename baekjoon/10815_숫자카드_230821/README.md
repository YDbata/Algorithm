# 10815 숫자카드

https://www.acmicpc.net/problem/10815

## 문제 이해

qsort로 정렬을 하고 이진탐색으로 풀이 하였다.
중간에 malloc이 백준에서 사용되지 않아 그냥 천만 배열을 만들고 시작하였다.

### 입력

첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.<br>
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.<br>
숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다.<br>
넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다.
<br>이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

### 출력

첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.

## 풀이

```c
#include <stdio.h>
#include <stdlib.h>

int num[10000000] = {0, }; //(int*)malloc(sizeof(int)*10000000);

int comp(const void* a, const void* b){
    if(*(int*)a > *(int*)b)
        return 1;
    else if(*(int*)b > *(int*)a)
        return -1;
    else
        return 0;
}

int binary(int m1, int start, int end){
    int center = (start+end)/2;

    if(start >= end){
        if(m1 != num[center])
            return 0;
        else
            return 1;
    }

    if(num[center] < m1)
        return binary(m1, center + 1, end);
    else if(num[center] > m1)
        return binary(m1, 0, center - 1);
    else
        return 1;

}

int main(){
    int n, m, m1;
    scanf("%d", &n);
    for(int i = 0; i < n;++i){
        scanf("%d", &num[i]);
    }
    qsort(num, n, 4, comp);

    scanf("%d", &m);
    for(int i = 0; i < m ;++i){
        scanf("%d", &m1);
        // 이진탐색(있으면 1, 없으면 0)
        printf("%d ", binary(m1, 0, n - 1));
    }
    //free(num);
    return 0;
}
```


![img.png](10815_c.png)