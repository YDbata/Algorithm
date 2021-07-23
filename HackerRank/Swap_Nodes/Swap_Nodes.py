import math
import os
import random
import re
import sys
sys.setrecursionlimit(100000)

# Complete the 'swapNodes' function below.
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
def add_n(que, idx, f, start):
    if f:
        t = que[start] - 1
        start += 1
    else:
        t = que.pop(start) - 1
    # print("t", t)
    if idx[t][0] != -1:
        que.append(idx[t][0])
    if idx[t][1] != -1:
        que.append(idx[t][1])
    return start


def inorder(idx, dep, order):
    if idx[dep][0] != -1:
        inorder(idx, idx[dep][0] - 1, order)
    order.append(dep + 1)
    if idx[dep][1] != -1:
        inorder(idx, idx[dep][1] - 1, order)

    return order


def swapNodes(indexes, queries):
    re = []
    for q in queries:
        que = [1]
        start = 0
        for i in range(len(indexes)):
            if (i + 1) % q == 0:
                f = 1
            else:
                f = 0
            num = len(que[start:])
            for i in range(num):
                start = add_n(que, indexes, f, start)
            # print(que, start)
            if start == len(que):
                break

        for i in que:
            tmp = indexes[i - 1][0]
            indexes[i - 1][0] = indexes[i - 1][1]
            indexes[i - 1][1] = tmp

        # print(indexes)
        re.append(inorder(indexes, 0, []))
    return re


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()