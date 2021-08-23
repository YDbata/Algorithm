def solution(lottos, win_nums):
    answer = []
    count = 0
    rank = 7
    for l in lottos:
        if l in win_nums:
            rank -= 1
        elif l == 0:
            count += 1
    if rank - count > 5:
        answer.append(6)
    else:
        answer.append(rank - count)

    if rank > 5:
        answer.append(6)
    else:
        answer.append(rank)

    return answer

## 명답
# def solution(lottos, win_nums):
#
#     rank=[6,6,5,4,3,2,1]
#
#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]