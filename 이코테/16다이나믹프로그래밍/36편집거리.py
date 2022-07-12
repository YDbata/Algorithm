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
for i in range(alen):
    if al[i] == -1:
        tmp += 1
    elif idx < al[i]:
        if tmp == 0:
            re += al[i] - idx
        else:
            re += tmp
            tmp = 0
        idx = al[i] + 1
    else:
        idx += 1

    # print(re, tmp, idx, al[i])

print(re + tmp)
'''sunxday
saturday'''