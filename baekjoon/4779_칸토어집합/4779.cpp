//
// Created by kiz75 on 2023-08-27.
//
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