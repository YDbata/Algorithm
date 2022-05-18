# 1번 힌트의 00:00:01 - 00:00:4 이면 3초라는 것이 [0,1,1,1,0]로 표현 되어야함


def trans_second(s):
    return (int(s[0:2])*60 + int(s[3:5]))*60 + int(s[-2:])

def solution(play_time, adv_time, logs):
    answer = ''
    if play_time == adv_time:
        return "00:00:00"

    logs_start = []
    total_time = (int(play_time[0:2])*60 + int(play_time[3:5]))*60 + int(play_time[-2:])
    time_line = [0 for _ in range(total_time + 1)]
    s_time_line = [0 for _ in range(total_time + 1)]

    for log in logs:
        tmp = log.split("-")
        slog = trans_second(tmp[0])
        elog = trans_second(tmp[1])
        for t in range(slog, elog):
            time_line[t] += 1
    s_time_line[0] = time_line[0]
    for time in range(1, total_time + 1):
        s_time_line[time] = s_time_line[time - 1] + time_line[time]

    # 최대값 찾기
    max_time = 0
    re = 0
    adv = trans_second(adv_time)
    # print(adv, s_time_line)
    for i in range(total_time - adv):
        if max_time < s_time_line[i + adv] - s_time_line[i]:
            max_time = s_time_line[i + adv] - s_time_line[i]
            re = i + 1

    if re//3600 < 10:
        answer += '0' + str(re//3600) + ':'
    else:
        answer += str(re // 3600) + ':'
    re = re%3600
    if re//60 < 10:
        answer += '0' + str(re //60) + ':'
    else:
        answer += str((re //60)%60) + ':'
    if re%60 < 10:
        answer += '0' + str(re%60)
    else:
        answer += str(re%60)

    # print(answer, re, max_time)
    # # print(s_time_line[3599:3599 + adv + 1])
    # print(s_time_line[trans_second("01:30:59") - 1:trans_second("01:45:14") + 2])
    return answer

# play_time = "99:59:59"
# adv_time = "25:00:00"
# logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]

play_time, adv_time, logs = "02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]
print(trans_second("01:30:59"), trans_second("01:45:14"))
solution(play_time, adv_time, logs)