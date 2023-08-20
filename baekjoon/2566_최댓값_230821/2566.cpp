//
// Created by kiz75 on 2023-08-21.
//
#include <stdio.h>

int main(){
    int max = 0;
    int n, locx = 1;
    int locy = 1;
    for(int i = 1 ; i < 10;++i){
        for(int j = 1; j < 10;++j){
            scanf("%d", &n);
            if (max < n){
                max = n;
                locx = i;
                locy = j;
            }
        }
    }
    printf("%d\n", max);
    printf("%d %d", locx, locy);
}