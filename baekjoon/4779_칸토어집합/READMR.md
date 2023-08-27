# 4779 칸토어 집합

https://www.acmicpc.net/problem/4779

## 문제 이해

3으로 나눈 값의 나머지가 1인 모든 수에 대해 빈칸을 출력하면 된다.<br>
파일의 끝이 주어지지 않으므로
```for(scanf() != EOF)```
구문으로 마무리 하였다.<br>

p.s pow는 그냥 만들어 봤다..

### 입력

입력을 여러 줄로 이루어져 있다. 각 줄에 N이 주어진다. 파일의 끝에서 입력을 멈춘다. N은 0보다 크거나 같고, 12보다 작거나 같은 정수이다.

### 출력

입력으로 주어진 N에 대해서, 해당하는 칸토어 집합의 근사를 출력한다.

## 풀이

```c
#include <stdio.h>

int my_pow(int tar, int num){
    int re = 1;
    for (int i = 0; i < num; ++i) {
        re *= tar;
    }
    return re;
}

void re(int n){
    int s = my_pow(3, n - 1);
    if(n == 0){
        printf("-");
        return;
    }

    re(n - 1);
    for(int i = 0;i < s;++i)
        printf(" ");

    re(n - 1);
}

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        re(n);
        printf("\n");
    }
    return 0;
}
```
![img.png](4779_c.png)
