//
// Created by kiz75 on 2023-09-04.
//
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int arraycmp(int *a, int *b, int size){
    //길이가 같은 배열 비교
    while(size){
        if(a[size - 1] != b[size - 1])
            return 0;

        size--;
    }
    return 1;
}


// want_len은 배열 want의 길이입니다.
// number_len은 배열 number의 길이입니다.
// discount_len은 배열 discount의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* want[], size_t want_len, int number[], size_t number_len, const char* discount[], size_t discount_len) {
    int answer = 0;
    int* number_l = (int *)malloc(sizeof(int)*want_len);

    for(int n = 0;n < number_len;++n)number_l[n] = 0;
    for(int i = 0;i<10;i++){
        for(int w = 0;w<want_len;w++){
            if(strcmp(want[w], discount[i]) == 0){
                number_l[w] += 1;
                break;
            }
        }
    }
    if(arraycmp(number_l, number, want_len))
        answer += 1;
    for(int i = 10;i<discount_len;i++){
        for(int w = 0;w<want_len;w++){
            if(strcmp(want[w], discount[i]) == 0){
                number_l[w] += 1;
                break;
            }
        }
        for(int w = 0;w<want_len;w++){
            if(strcmp(want[w], discount[i - 10]) == 0){
                number_l[w] -= 1;
                break;
            }
        }
        if(arraycmp(number_l, number, want_len))
            answer += 1;
    }


    return answer;
}