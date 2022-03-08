import sys

def bi(s, e, loc):
    global b_tree, m
    if e < s:
        return 1

    md = (e - s)//2
    b_tree[loc] = b[s + md]
    if s != e:
        if 2*loc + 1 < m:
            bi(s, s + md - 1, 2*loc + 1)
        if 2*(loc + 1) < m:
            bi(s + md + 1, e, 2*(loc + 1))

if __name__=="__main__":
    t = int(input())
    m = 0
    for _ in range(t):
        n, m = map(int, input().split())
        a = tuple(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))
        b.sort()
        b_tree = [0 for _ in range(m)]
        root = b[0]
        rsum = 0
        bi(0, m - 1, 0)

        for at in a:
            node = 0
            dt = 10**9
            tmp_sum = b_tree[node]
            while node < m:
                if dt == abs(b_tree[node] - at):
                    if tmp_sum > b_tree[node]:
                        tmp_sum = b_tree[node]
                    break
                elif dt > abs(b_tree[node] - at):
                    dt = abs(b_tree[node] - at)
                    tmp_sum = b_tree[node]

                if at == b_tree[node]:
                    tmp_sum = at
                    break
                elif at > b_tree[node]:
                    node = 2*(node + 1)
                else:
                    node = 2*node + 1
            rsum += tmp_sum

        print(rsum)