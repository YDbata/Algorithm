import math

if __name__ == "__main__":
    n, m = map(int, input().split())

    tree = list(map(int, input().split()))
    tree.append(0)
    tree.sort(reverse=True)
    t_sum = 0
    t_count = 1
    re = 0
    for i in range(n):
        if t_sum + t_count*(tree[i] - tree[i + 1]) >= m:
            re += math.ceil((m - t_sum)/t_count)
            t_sum += math.ceil((m - t_sum)/t_count)*t_count
            break
        else:
            re += (tree[i] - tree[i + 1])
            t_sum += t_count*(tree[i] - tree[i + 1])
        t_count += 1

    print(tree[0] - re)