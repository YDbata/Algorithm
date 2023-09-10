# 2346 풍선터뜨리기

https://www.acmicpc.net/problem/2346

## 문제 이해

코테 언어를 C++(혹은 C#)로 바꾸기로 결심하고 처음으로 연결리스트를 구조체로 작성하여 풀어본 문제<br>
처음에는 반복문으로 작성하였으나 시간초과가 떴다.<br>

때문에 문제를 보고 연결리스트를 떠올렸고 이번에는 틀렸었다.<br>
틀린 이유는 초기화를 제대로 해주지 않아서 였다.<br>
초기화 해주는 함수를 만들려다가 간단해보여서 안만들었더니 이런 일이 생겼다.<br>
따로 init함수를 만들어서 쓰는 이유가 있었다. 이번을 계기로 다시한번 함수의 중요성을 알아간다. 

### 입력

첫째 줄에 자연수 N(1 ≤ N ≤ 1,000)이 주어진다. 다음 줄에는 차례로 각 풍선 안의 종이에 적혀 있는 수가 주어진다. 종이에 0은 적혀있지 않다.

### 출력

첫째 줄에 터진 풍선의 번호를 차례로 나열한다.

## 풀이

```c
#include <stdio.h>
#include <iostream>

typedef struct tarNode{
    struct tarNode* nNode;
    struct tarNode* pNode;
    int num;
    int data;
}tNode;

typedef struct LL{
    tNode* RootNode = (tNode*)malloc(sizeof(tNode));
    int iCount;
} LL;


int main(){
    int n, x, count, tmp;
    //int list[1000];
    int m;
    LL* root = (LL*)malloc(sizeof(LL));
    //int re[1000] = {0, };
    //bool flag = true;
    scanf("%d", &n);
    tNode* rnode = (tNode*)malloc(sizeof(tNode));
    scanf("%d", &m);
    rnode->data = m;
    rnode->num = 1;
    rnode->pNode = nullptr;
    rnode->nNode = nullptr;
    root->RootNode = rnode;
    root->iCount = 1;
    for(int i = 1;i<n;++i){
        tNode* tnode = (tNode*)malloc(sizeof(tNode));
        scanf("%d", &m);
        tnode->data = m;
        tnode->pNode = rnode;
        rnode->nNode = tnode;
        tnode->nNode = nullptr;
        tnode->num = i + 1;
        root->iCount++;
        rnode = tnode;
    }


    // 마지막 좌표에서 nNode를 root로 root의 p노드를 마지막 노드로
    rnode->nNode = root->RootNode;
    (root->RootNode)->pNode = rnode;
    // 현재 좌표
    tNode* nownode = (tNode*)malloc(sizeof(tNode));
    nownode = root->RootNode;
    x = 0;
    printf("%d ", nownode->num);
    root->iCount--;
    while(root->iCount != 0){
        root->iCount--;

        (nownode->nNode)->pNode = nownode->pNode;
        nownode->pNode->nNode = nownode->nNode;
        x = nownode->data;
        if(x > 0){
            for(int i = 0;i < x;i++){
                nownode = nownode->nNode;
            }
        } else{
            for(int i = 0;i > x;i--){
                nownode = nownode->pNode;
            }
        }
        printf("%d ", nownode->num);
    }


    return 0;
}
```

![img.png](2346_cpp.png)