//
// Created by kiz75 on 2023-08-27.
//
#include <stdio.h>

int star(int n, int x, int y){
    if((x/n)%3==1 && (y/n)%3==1){
        printf(" ");
    }
    else{
        if(n == 1)
            printf("*");
        else
            star(n/3, x, y);
    }
    return 0;
}


int main(){
    int n;
    scanf("%d", &n);
    //star10(n, 0, 0);

    for(int x = 0; x < n;++x){
        for(int y = 0;y < n;++y) {
            star(n/3, x, y);
        }
        printf("\n");
    }
    return 0;
}