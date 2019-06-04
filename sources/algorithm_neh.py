from algorithm_cmax import c_max, cmax


def NEH(jobs):
    v_jobslist = []  # virtal jobs list (only 1 machine, time=time(0)+time(1)+...+time(n))
    for i in range(len(jobs)):
        sum = 0
        for j in range(jobs[i].size):
            sum = sum + jobs[i].time(j)
        v_jobslist.append([sum, len(jobs) - i])

    v_jobslist.sort(reverse=True)
    for i in range(len(v_jobslist)):
        v_jobslist[i][1] = (v_jobslist[i][1] - len(v_jobslist)) * (-1)

    perm = []  # best queue
    perm.append(v_jobslist[0][1])  # first job (max time)
    cmaxlist = []
    perm_list = []
    tmp_perm = []  # temporary queue

    for k in range(len(perm)):
        tmp_perm.append(perm[k])  # tmp_perm=perm
    for i in range(1, len(v_jobslist)):
        for j in range(i + 1):
            tmp_perm.insert(j, v_jobslist[i][1])  # add on position i
            # print(" PERM: ",tmp_perm, "CMAX: ", c_max(tmp_perm, jobs))
            cmaxlist.append(c_max(tmp_perm, jobs))  # and check time using cmax
            perm_list.append(tmp_perm)
            tmp_perm = []  # tmp_perm=perm
            for k in range(len(perm)):
                tmp_perm.append(perm[k])

        # Queue update!
        cmaxmin = cmaxlist[0]
        index = 0
        for j in range(1, len(cmaxlist)):  # min(cmaxlist)
            if cmaxlist[j] < cmaxmin:
                cmaxmin = cmaxlist[j]
                index = j
        perm = perm_list[index]  # and update...
        cmaxlist = []
        perm_list = []
        tmp_perm = []  # tmp_perm=perm
        for k in range(len(perm)):
            tmp_perm.append(perm[k])
    return perm




def bestperm(perm, index, jobs):
    Cd, Cw = cmax(perm, jobs)
    cmaxlist = []
    times = []
    td = [0] * (jobs[0].size + 1)

    for i in range(len(perm) + 1):
        for j in range(1, len(td)):
            td[j] = max(td[j - 1], Cd[i][j]) + jobs[index].time(j - 1)
            times.append(td[j] + Cw[i + 1][j])
        cmaxlist.append(max(times))
        times = []
        td = [0] * (jobs[0].size + 1)

    mintime = max(cmaxlist)
    ind = 0
    for i in range(len(cmaxlist)):  # looking for min cmax
        if cmaxlist[i] < mintime:
            mintime = cmaxlist[i]
            ind = i  # and index of min cmax

    # print(cmaxlist,'   wstawiam ',index, ' na pozycje ', ind)
    perm.insert(ind, index)  # new perm (+index on ind position)
    return perm


def QNEH(jobs):
    v_jobslist = []  # virtal jobs list (only 1 machine, time=time(0)+time(1)+...+time(n))
    for i in range(len(jobs)):
        sum = 0
        for j in range(jobs[i].size):
            sum = sum + jobs[i].time(j)
        v_jobslist.append([sum, len(jobs) - i])

    v_jobslist.sort(reverse=True)
    for i in range(len(v_jobslist)):
        v_jobslist[i][1] = (v_jobslist[i][1] - len(v_jobslist)) * (-1)

    perm = []  # best queue
    perm.append(v_jobslist[0][1])  # first job (max time)
    for i in range(1, len(v_jobslist)):
        perm = bestperm(perm, v_jobslist[i][1], jobs)
    return perm


def deljob(perm, jobs, last):
    Cd, Cw = cmax(perm, jobs)
    cmaxlist = []
    t = [0] * (jobs[0].size + 1)
    for i in range(len(perm)):
        for j in range(len(t)):
            t[j] = Cd[i][j] + Cw[i + 2][j]
        cmaxlist.append([max(t), len(perm) - i])
        t = [0] * (jobs[0].size + 1)

    cmaxlist.sort(reverse=True)  #

    for i in range(len(cmaxlist)):
        cmaxlist[i][1] = (cmaxlist[i][1] - len(perm)) * (-1)

    if cmaxlist[0][1] == last:
        ind = cmaxlist[1][1]
    else:
        ind = cmaxlist[0][1]
    num = perm.pop(ind)

    return perm, num


def mod4QNEH(jobs):
    v_jobslist = []  # virtal jobs list (only 1 machine, time=time(0)+time(1)+...+time(n))
    for i in range(len(jobs)):
        sum = 0
        for j in range(jobs[i].size):
            sum = sum + jobs[i].time(j)
        v_jobslist.append([sum, len(jobs) - i])

    v_jobslist.sort(reverse=True)
    for i in range(len(v_jobslist)):
        v_jobslist[i][1] = (v_jobslist[i][1] - len(v_jobslist)) * (-1)

    perm = []  # best queue
    perm.append(v_jobslist[0][1])  # first job (max time)
    for i in range(1, len(v_jobslist)):
        perm = bestperm(perm, v_jobslist[i][1], jobs)
        perm, num = deljob(perm, jobs, v_jobslist[i][1])
        perm = bestperm(perm, num, jobs)
    return perm


def CPM(perm, jobs):
    EF = [[0] * (jobs[0].size + 2) for i in range(len(perm) + 2)]  #

    cp = []

    for j in range(1, jobs[0].size + 1):  # machine number+1
        for i in range(1, len(perm) + 1):  # job number+1
            EF[i][j] = max(EF[i][j - 1], EF[i - 1][j]) + jobs[perm[i - 1]].time(j - 1)  # coming

    maxef = max(max(EF))

    LS = [[maxef] * (jobs[0].size + 2) for i in range(len(perm) + 2)]  #
    for j in range(jobs[0].size, 0, -1):  # machine number+1
        for i in range(len(perm), 0, -1):  # job number+1
            LS[i][j] = min(LS[i][j + 1], LS[i + 1][j]) - jobs[perm[i - 1]].time(j - 1)  # outgoing
    for j in range(1, jobs[0].size + 1):
        for i in range(1, len(perm) + 1):
            if LS[i][j] + jobs[perm[i - 1]].time(j - 1) == EF[i][j]:
                cp.append([jobs[perm[i - 1]].time(j - 1), i - 1, j - 1])
    return cp


def mod1QNEH(jobs):
    v_jobslist = []  # virtal jobs list (only 1 machine, time=time(0)+time(1)+...+time(n))
    for i in range(len(jobs)):
        sum = 0
        for j in range(jobs[i].size):
            sum = sum + jobs[i].time(j)
        v_jobslist.append([sum, len(jobs) - i])

    v_jobslist.sort(reverse=True)
    for i in range(len(v_jobslist)):
        v_jobslist[i][1] = (v_jobslist[i][1] - len(v_jobslist)) * (-1)

    perm = []  # best queue
    perm.append(v_jobslist[0][1])  # first job (max time)
    for i in range(1, len(v_jobslist)):
        perm = bestperm(perm, v_jobslist[i][1], jobs)
        cp = CPM(perm, jobs)
        cp.sort(reverse=True)
        perm, num = deljob(perm, jobs, cp[0][1])
        perm = bestperm(perm, num, jobs)
    return perm


def mod2QNEH(jobs):
    v_jobslist = []  # virtal jobs list (only 1 machine, time=time(0)+time(1)+...+time(n))
    for i in range(len(jobs)):
        sum = 0
        for j in range(jobs[i].size):
            sum = sum + jobs[i].time(j)
        v_jobslist.append([sum, len(jobs) - i])

    v_jobslist.sort(reverse=True)
    for i in range(len(v_jobslist)):
        v_jobslist[i][1] = (v_jobslist[i][1] - len(v_jobslist)) * (-1)

    perm = []  # best queue
    perm.append(v_jobslist[0][1])  # first job (max time)
    for i in range(1, len(v_jobslist)):
        perm = bestperm(perm, v_jobslist[i][1], jobs)
        cp = CPM(perm, jobs)
        sum_cp = [0] * len(perm)  #
        maxsum = 0
        ind = 0
        for i in range(len(perm)):
            sum_cp[cp[i][1]] += cp[i][0]
        for i in range(len(sum_cp)):
            if maxsum < sum_cp[i]:
                maxsum = sum_cp[i]
                ind = i

        perm, num = deljob(perm, jobs, ind)
        perm = bestperm(perm, num, jobs)
    return perm


def mod3QNEH(jobs):
    v_jobslist = []  # virtal jobs list (only 1 machine, time=time(0)+time(1)+...+time(n))
    for i in range(len(jobs)):
        sum = 0
        for j in range(jobs[i].size):
            sum = sum + jobs[i].time(j)
        v_jobslist.append([sum, len(jobs) - i])

    v_jobslist.sort(reverse=True)
    for i in range(len(v_jobslist)):
        v_jobslist[i][1] = (v_jobslist[i][1] - len(v_jobslist)) * (-1)

    perm = []  # best queue
    perm.append(v_jobslist[0][1])  # first job (max time)
    for i in range(1, len(v_jobslist)):
        perm = bestperm(perm, v_jobslist[i][1], jobs)
        cp = CPM(perm, jobs)
        sum_cp = [0] * len(perm)  #
        maxsum = 0
        ind = 0
        for i in range(len(perm)):
            sum_cp[cp[i][1]] += 1
        for i in range(len(sum_cp)):
            if maxsum < sum_cp[i]:
                maxsum = sum_cp[i]
                ind = i

        perm, num = deljob(perm, jobs, ind)
        perm = bestperm(perm, num, jobs)
    return perm
