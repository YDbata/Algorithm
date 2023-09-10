//
// Created by kiz75 on 2023-09-10.
//
#include <stdio.h>

int prime_list[1000000] = {0,}; // 소수 리스트 소수 = 0, 아닌경우 1
int main(){
    int t, x;
    int re, maxx = 0;
    int list[100];

    scanf("%d", &t);
    for(int i = 0;i <t;++i){
        scanf("%d", &list[i]);
        if(list[i] > maxx)
            maxx = list[i];
    }
    prime_list[0] = 1;
    prime_list[1] = 1;
    // maxx값 기준 에라토스테네스의 체 시작
    for(int i =2;i < maxx;i++){
        if(prime_list[i] == 0){
            x = 2;
            while(i*x < maxx){
                prime_list[i*x++] = 1;
            }
        }
    }

    // 각 수마다 골드바흐 시작
    for(int j = 0;j < t;j++){
        re = 0;
        for(int z = 2;z < list[j]/2 + 1;z++){
            if(prime_list[z] == 0){
                if(prime_list[list[j] - z] == 0 )
                    re++;
            }
        }
        printf("%d\n", re);
    }

    return 0;
}
