//
// Created by kiz75 on 2023-09-10.
//
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