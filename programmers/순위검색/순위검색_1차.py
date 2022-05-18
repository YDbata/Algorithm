from collections import defaultdict
# 정확도 100%
# 효율성 0%

def solution(info, query):
    answer = []
    score = defaultdict(list)
    for i in range(len(info)):
        info[i] = info[i].split(' ')
        score[info[i][-1]].append(info[i][:-1])
    # print(score)
    for q in query:
        q = q.replace("-", "").replace(' and', '')
        tmp = q.split(' ')
        # print(tmp)
        re = 0
        for s in score.items():
            if int(s[0]) >= int(tmp[-1]):
                for i in s[1]:
                    f = 1
                    for q in range(4):
                        if not tmp[q] in i[q]:
                            f = 0
                            break
                    if f:
                        re += 1
        answer.append(re)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# [1,1,1,1,2,4]
solution(info, query) # dic["javabackendjuniorpizza"] = [150]