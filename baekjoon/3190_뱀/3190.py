def is_safe(x, y, n):
    if -1< x <n and -1 < y < n:
        return 1
    else:
        return 0

if __name__=="__main__":
    n = int(input())
    k = int(input())
    apple_list = []

    for a in range(k):
        apple_list.append(list(map(int, input().split())))

    l = int(input())
    queue = []
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    loc = [0,0]
    d = 0
    safe = 1
    count = 1
    pre_x = 0
    x = 0
    x_que = []
    for xc in range(l):
        x, c = input().split()
        x = int(x)
        x_que.append((x, c))
    x_que.append((1000001, ''))

    for i in range(1000000):
        if is_safe(loc[0] + dx[d], loc[1] + dy[d], n):


            queue.append(loc)
            if [loc[0] + dx[d], loc[1] + dy[d]] in queue:
                break

            count += 1
            if [loc[0] + dx[d] + 1, loc[1] + dy[d] + 1] in apple_list:
                del apple_list[apple_list.index([loc[0] + dx[d] + 1, loc[1] + dy[d] + 1])]
                loc = [loc[0] + dx[d], loc[1] + dy[d]]
            else:
                loc = [loc[0] + dx[d], loc[1] + dy[d]]
                queue.pop(0)

        else:
            break

        if x_que[0][0] == i + 1:
            if x_que[0][1] == 'D':
                d -= 1
                if d < 0:
                    d = 3
            else:
                d += 1
                if d > 3:
                    d = 0

            x_que.pop(0)

    print(count)