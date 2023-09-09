# 1735 분수합

https://www.acmicpc.net/problem/1735

## 문제 이해

통분 후에 분수계산을 하고 약분은<br>
에라토스테네스의 체를 이용하여 소수를 구분하고 진행하였다.

때문에 시간이 오래 걸린거 같아 다른 풀이도 찾아봤다.<br> 
에라토스테네스의 체를 쓰나 안쓰나 크게 시간차가 없었다.<br>
그러면 안쓰는게 짧고 좋은거같기도 하다.

### 입력

첫째 줄과 둘째 줄에, 각 분수의 분자와 분모를 뜻하는 두 개의 자연수가 순서대로 주어진다. 입력되는 네 자연수는 모두 30,000 이하이다.

### 출력

첫째 줄에 구하고자 하는 기약분수의 분자와 분모를 뜻하는 두 개의 자연수를 빈 칸을 사이에 두고 순서대로 출력한다.

## 풀이

```c
#include <stdio.h>

int main(){
    int n,m;
    int x, y, denom, mole, maxd;
    int prime_list[30001] = {0,};

    scanf("%d %d", &n, &m);
    scanf("%d %d", &x, &y);

    mole = (n*y) + (x*m);
    denom = y*m;

    if(x < y){
        maxd = y;
    } else{
        maxd = x;
    }
    // 에라토스테네스의 채
    int i = 2;
    prime_list[0] = 1;
    prime_list[1] = 1;

    while(i < maxd + 1){
        if(prime_list[i] == 0){
            for(int j = 2;j*i < maxd;j++){
                prime_list[j*i] = 1;
            }
        }
        ++i;
    }

    // 약분
    i = 2;
    while(i < maxd + 1){
        if(!prime_list[i]){
            while(denom%i == 0 && mole%i == 0){
                denom /= i;
                mole /= i;
            }
        }
        ++i;
    }
    printf("%d %d", mole, denom);
    return 0;
}
```

![img.png](1735_c.png)