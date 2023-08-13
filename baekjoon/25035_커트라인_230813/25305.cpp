//
// Created by kiz75 on 2023-08-13.
//
#include <stdio.h>

int main() {
    int n, k, x, tmpk;
    int score[10001] = {0,};
    int re;

    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        score[x] += 1;
    }
    tmpk = 0;
    for(re = 10001;re>=0;re--){
        tmpk += score[re];
        if(tmpk >= k){
            printf("%d", re);
            break;
        }
    }
}