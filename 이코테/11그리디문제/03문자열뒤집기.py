sl = input()
f_l = [0, 0]
flag = sl[0]
f_l[int(flag)] = 1

for s in sl[1:]:
    if s != flag:
        flag = s
        f_l[int(flag)] += 1

print(min(f_l))
