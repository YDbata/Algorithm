//
// Created by kiz75 on 2023-08-21.
//
#include <stdio.h>
#include <stdlib.h>

int num[10000000] = {0, }; //(int*)malloc(sizeof(int)*10000000);

int comp(const void* a, const void* b){
    if(*(int*)a > *(int*)b)
        return 1;
    else if(*(int*)b > *(int*)a)
        return -1;
    else
        return 0;
}

int binary(int m1, int start, int end){
    int center = (start+end)/2;

    if(start >= end){
        if(m1 != num[center])
            return 0;
        else
            return 1;
    }

    if(num[center] < m1)
        return binary(m1, center + 1, end);
    else if(num[center] > m1)
        return binary(m1, 0, center - 1);
    else
        return 1;

}

int main(){
    int n, m, m1;
    scanf("%d", &n);
    for(int i = 0; i < n;++i){
        scanf("%d", &num[i]);
    }
    qsort(num, n, 4, comp);

    scanf("%d", &m);
    for(int i = 0; i < m ;++i){
        scanf("%d", &m1);
        // 이진탐색(있으면 1, 없으면 0)
        printf("%d ", binary(m1, 0, n - 1));
    }
    //free(num);
    return 0;
}