//
// Created by kiz75 on 2023-08-12.
//
#include <stdio.h>

int main(){
    int a, b, c, d, e, f;
    int x, y;
    scanf("%d %d %d %d %d %d", &a,&b,&c,&d,&e,&f);
    // x에 0 대입

    if(b == 0){
        x = c/a;
        printf("%d %d", x, (f - d*x)/e);
    }
    else{
        // for문으로 1, -1부터 999, -999까지 x에 대입
        for(x = 0;x < 1000;++x){
            y = (c - a*x)/b;
            if(d*x + e*y == f){
                printf("%d %d", x, y);
                break;
            }
            else{
                y = (c - a*(-x))/b;
                if(d*(-x) + e*y == f){
                    printf("%d %d",-x,y);
                    break;
                }
            }

        }

    }
}
