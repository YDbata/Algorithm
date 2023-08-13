//
// Created by kiz75 on 2023-08-14.
//
#include<stdio.h>
#include<stdlib.h>

int N;

typedef struct point {
    int x;
    int x_;
    int order;
} POINT;

POINT points[1000020];

int compare(const void* first, const void* second) {
    if (((POINT*)first)->x < ((POINT*)second)->x)
        return -1;
    else if (((POINT*)first)->x > ((POINT*)second)->x)
        return 1;
    else
        return 0;
}

int compare1(const void* first, const void* second) {
    if (((POINT*)first)->order < ((POINT*)second)->order)
        return -1;
    else if (((POINT*)first)->order > ((POINT*)second)->order)
        return 1;
    else
        return 0;
}

int main(void) {

    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%d", &points[i].x);
        points[i].order = i;
    }

    qsort(points, N, sizeof(POINT), compare);

    for (int i = 0; i < N; i++) {

        if (i == 0) {
            points[i].x_ = 0;
        }
        else {
            if (points[i - 1].x == points[i].x) {
                points[i].x_ = points[i - 1].x_;
            }
            else {
                points[i].x_ = points[i - 1].x_+1;
            }
        }
    }

    qsort(points, N, sizeof(POINT), compare1);

    for (int i = 0; i < N; i++) {
        printf("%d ", points[i].x_);
    }
    printf("\n");
}