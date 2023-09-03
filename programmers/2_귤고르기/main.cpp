//
// Created by kiz75 on 2023-09-04.
//
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int comp(const void *n, const void *m){
    int a = *(int *)n;
    int b = *(int *)m;
    if(a > b)
        return -1;
    else if(b>a)
        return 1;
    else
        return 0;
}


// tangerine_len은 배열 tangerine의 길이입니다.
int solution(int k, int tangerine[], size_t tangerine_len) {
    int answer = 0;
    int* tan_l = (int*)malloc(sizeof(int)*tangerine_len);
    int* tan_count_l = (int*)malloc(sizeof(int)*tangerine_len);
    int type_tan = 0;
    int tan_lcount = 0;
    bool tan_bool;

    for(int i = 0;i < tangerine_len;++i){
        tan_bool = true;
        for(int j = 0;j < tan_lcount;++j){
            if(tangerine[i] == tan_l[j]){
                tan_count_l[j] += 1;
                tan_bool = false;
            }

        }
        if(tan_bool){
            tan_l[tan_lcount] = tangerine[i];
            tan_count_l[tan_lcount++] = 1;
        }

    }

    qsort(tan_count_l, tan_lcount, sizeof(int), comp);

    while(k>type_tan){
        type_tan += tan_count_l[answer++];
    }
    return answer;
}

int main(){
    int list[8] = {1, 3, 2, 5, 4, 5, 2, 3};
    printf("%d\n",solution(6,list,8));
}