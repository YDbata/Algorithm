# 10988 팰린드롬인지 확인하기

https://www.acmicpc.net/problem/10988

## 문제 이해

스피드런 문제<br>
8분 정도 걸렸다. 조금 더 시간을 줄이면 좋을 것같고<br>
포인터를 이용해봐야겠다.

### 입력

첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

### 출력

첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.

## 풀이

```c
#include <stdio.h>

int main(){
    char str[100];
    int end, start = 0;
    scanf("%s", str);
    for(end = 0;str[end]!='\0';++end);
    end -= 1;
    while(start < end){
        if(str[start] != str[end]){
            printf("%d", 0);
            return 0;
        }
        ++start;
        --end;
    }
    printf("%d", 1);
}
```


![img.png](10988_c.png)