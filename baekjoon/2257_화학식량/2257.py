s = input()

atom_dic = {'H': 1, 'C': 12, 'O': 16}
stack = []
head = -1

for i in s:
    if i == '(':
        stack.append(i)
        head += 1
    elif i.isalpha():
        stack.append(atom_dic[i])
        head += 1
    elif i.isdigit():
        stack[head] *= int(i)
    else:
        tmp = 0
        while stack[head] != '(':
            tmp += stack.pop()
            head -= 1
        stack[head] = tmp

print(sum(stack))