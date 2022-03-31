import sys

N, M = map(int, sys.stdin.readline().split())
start_node = int(input())
edge = []

for _ in range(M):
    edge.append(list(map(int, input().split())))

