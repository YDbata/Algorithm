n = input()

mid = len(n)//2

if sum([int(i) for i in n[:mid]]) == sum([int(i) for i in n[mid:]]):
    print("LUCKY")
else:
    print("READY")
