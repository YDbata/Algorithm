//
// Created by kiz75 on 2023-09-09.
//
#include <stdio.h>

int main(){
    int n,m;
    int x, y, denom, mole, maxd;

    scanf("%d %d", &n, &m);
    scanf("%d %d", &x, &y);

    mole = (n*y) + (x*m);
    denom = y*m;

    if(x < y){
        maxd = y;
    } else{
        maxd = x;
    }
    // 에라토스테네스의 체

    // 약분
    int i = 2;
    while(i < maxd + 1){
        if(denom%i == 0 && mole%i == 0){
            denom /= i;
            mole /= i;
        }else{
            ++i;
        }
    }
    printf("%d %d", mole, denom);
    return 0;
}
