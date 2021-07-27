def combi(ml, m, re, b, start):
    if m == 0:
        tmp = 0
        for i in range(nl):
            tmp += distance[i][min(b, key=lambda x: distance[i][x])]

        if tmp < re:
            re = tmp
    else:
        for i in range(start, ml):
            b.append(i)
            re = combi(ml, m - 1, re, b, i + 1)
            b.pop()

    return re

if __name__=="__main__":
    n, m = map(int, input().split())


    n_list = []
    m_list = []
    for r in range(n):
        tmp = list(map(int, input().split()))
        for c in range(n):
            if tmp[c] == 1:
                n_list.append((r, c))
            elif tmp[c] == 2:
                m_list.append((r, c))

    ml = len(m_list)
    nl = len(n_list)
    distance = [[0 for _ in range(ml)] for _ in range(nl)]
    for r in range(nl):
        for c in range(ml):
            distance[r][c] = abs(n_list[r][0] - m_list[c][0]) + abs(n_list[r][1] - m_list[c][1])

    print(combi(ml, m, n*nl, [], 0))