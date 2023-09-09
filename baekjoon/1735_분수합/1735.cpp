//
// Created by kiz75 on 2023-09-09.
//
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
            if(denom%i == 0 && mole%i == 0){
                denom /= i;
                mole /= i;
            }else{
                ++i;
            }
        } else{
            ++i;
        }
    }
    printf("%d %d", mole, denom);
    return 0;
}