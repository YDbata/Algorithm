a = input()
b = input()
alen = len(a)
al = [-1 for _ in range(alen)]

for aa in range(alen):
    for bb in range(len(b)):
        if a[aa] == b[bb]:
            al[aa] = bb

re = 0
tmp = 0
idx = 0
for i in range(alen - 1):
    if al[i] == -1:
        tmp += 1
    elif idx < al[i]:
        if tmp == 0:
            re += al[i] - idx
        else:
            tmp = 0
        idx = al[i]

    idx += 1
