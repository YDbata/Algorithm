//
// Created by kiz75 on 2023-09-04.
//
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


int solution(char* s) {
    int answer = 0;
    int s_len = strlen(s);
    int left; int right;

    for(int start = 0; start < s_len; start++){
        for (int last = s_len; last > answer; last--){
            left = start;
            right = left + last - 1;
            while (s[left] == s[right] && left < right){
                left ++;
                right --;
            }
            if(left >= right){
                if(answer < last){
                    answer = last;
                    break;
                }
            }
        }
    }

    return answer;
}

int main(){
    printf("%d",solution("abacde"));
}