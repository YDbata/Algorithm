s = input()

sum_n = 0
new_s = ""
for i in s:
    if i.isalpha():
        new_s += i
    else:
        sum_n += int(i)

new_s = sorted(new_s)
print(*sorted(new_s), sep="", end="")
print(str(sum_n))

'''
AJKDLSI412K4JSJ9D
ADDIJJJKKLSS20
'''
