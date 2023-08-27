# 11659 구간 합 구하기4

https://www.acmicpc.net/problem/11659

## 문제 이해

그냥 누적 합을 구한 후 인덱스에 따라 빼주면 되는 문제<br>
난이도보다 쉬운듯...

### 입력

첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

### 출력

총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

## 풀이

```c
#include <stdio.h>

int main(){
    int n, m, num;
    int ii, jj;
    int num_l[100000];
    scanf("%d %d", &n, &m);

    for(int i = 1;i < n + 1;++i){
        scanf("%d", &num);
        num_l[i] = num_l[i - 1] + num;
    }
    for(int j = 0;j < m;++j){
        scanf("%d %d", &ii,&jj);
        printf("%d\n", num_l[jj] - num_l[ii - 1]);
    }
}
```

![img.png](11659_c.png)