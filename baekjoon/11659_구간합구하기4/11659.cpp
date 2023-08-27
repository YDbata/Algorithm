//
// Created by kiz75 on 2023-08-27.
//
#include <stdio.h>

int main(){
    int n, m, num;
    int ii, jj;
    int num_l[100000];
    scanf("%d %d", &n, &m);

    for(int i = 1;i < n + 1;++i){
        scanf("%d", &num);
        num_l[i] = num_l[i - 1] + num;
    }
    for(int j = 0;j < m;++j){
        scanf("%d %d", &ii,&jj);
        printf("%d\n", num_l[jj] - num_l[ii - 1]);
    }
}