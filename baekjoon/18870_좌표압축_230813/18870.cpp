#include <stdio.h>

int xarr[999999];
int re[999999] = { 0, };
int main() {
    int n;
    scanf("%d", &n);
    // scan을 하나 받을 때마다 앞에서 부터 비교하고 압축 적용
    for (int i = 0; i < n; i++) {
        scanf("%d", &xarr[i]);
        for (int j = 0; j < i; j++) {
            if (xarr[j] < xarr[i]) {
                re[i] += 1;
            }
            else if (xarr[j] > xarr[i]) {
                re[j] += 1;
            }
        }
    }

    for (int z = 0; z < n; z++) {
        printf("%d ", re[z]);
    }
    return 0;
}