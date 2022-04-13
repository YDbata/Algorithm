
s = list(map(int, list(input())))
re = s[0]
for sn in s[1:]:
    if sn == 0 or re == 0:
        re += sn
    else:
        re *= sn

print(re)
