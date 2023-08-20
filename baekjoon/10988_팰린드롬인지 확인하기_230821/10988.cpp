//
// Created by kiz75 on 2023-08-21.
//
#include <stdio.h>

int main(){
    char str[100];
    int end, start = 0;
    scanf("%s", str);
    for(end = 0;str[end]!='\0';++end);
    end -= 1;
    while(start < end){
        if(str[start] != str[end]){
            printf("%d", 0);
            return 0;
        }
        ++start;
        --end;
    }
    printf("%d", 1);
}
