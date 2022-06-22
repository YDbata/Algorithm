n = int(input())

stu = []

for i in range(n):
    student = input().split()
    student[1:] = list(map(int, student[1:]))
    stu.append(student)

stu.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for s in stu:
    print(s[0])