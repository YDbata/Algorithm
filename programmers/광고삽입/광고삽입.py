def compare_t(a, b1, b2, c1, c2):
    tmp1 = 0
    tmp2 = 59
    if a == b1:
        tmp1 = c1
    if a == b2:
        tmp2 = c2

    return tmp1, tmp2


def solution(play_time, adv_time, logs):
    answer = ''
    if play_time == adv_time:
        return "00:00:00"

    logs_start = []
    time_line = [[[0 for _ in range(60)] for _ in range(60)] for _ in range(int(play_time[0:2]) + 1)]

    for log in logs:
        tmp = log.split("-")
        shous, smins, ssecs = map(int, tmp[0].split(":"))
        logs_start.append([shous, smins, ssecs, tmp[0]])
        ehous, emins, esecs = map(int, tmp[1].split(":"))
        print("e",ehous, emins, esecs)
        for h in range(shous, ehous + 1):
            hsmin, hemin = compare_t(h, shous, ehous, smins, emins)
            for m in range(hsmin, hemin + 1):
                mssec, mesec = compare_t(m, smins, emins, ssecs, esecs)
                for s in range(mssec, mesec + 1):
                    # print(h, m ,s)
                    time_line[h][m][s] += 1

    # 최대값 찾기
    time_sum = []
    adv = list(map(int, adv_time.split(":")))
    ph, pm, ps = map(int, play_time.split(":"))
    for n, ls in enumerate(logs_start):
        tmp_sum = 0
        print(adv, '\n', ls)
        ts = (adv[2] + ls[2]) % 60
        tm = adv[1] + ls[1] + (1 if (adv[2] + ls[2]) // 60 > 0 else 0)
        th = adv[0] + ls[0] + (1 if tm // 60 > 0 else 0)
        tm = tm % 60
        print("t", th, tm, ts)
        if th > ph:
            print("d")
            continue
        for h in range(ls[0], th + 1):
            smin, emin = compare_t(h, ls[0], th, ls[1], tm)
            for m in range(smin, emin + 1):
                ssec, esec = compare_t(m, ls[1], tm, ls[2], ts)
                for s in range(ssec, esec + 1):
                    tmp_sum += time_line[h][m][s]
        logs_start[n].append(tmp_sum)
    re = max(logs_start, key = lambda x : (x[4], -x[0], -x[1]))

    return re[3]

play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
solution(play_time, adv_time, logs)