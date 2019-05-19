from job import *


def c_max(queue, jobs=[Job]):
    """
    Simulate process
    :param queue: An order to simulate total time
    :param jobs:  list(Job) contains times on machines
    :return: Total Time
    """
    def sim_time(job, machines_diary):
        """
        Simulate job
        :param job: times on machines
        :param machines_diary: last done job on machines
        :return:
        """
        machines_list = range(0, np.shape(job.time_on_machine)[0])
        time = 0

        for machine in machines_list:
            delay = machines_diary[machine] - time  # job delay
            if delay < 0:
                delay = 0
            time = time + delay + job.time(machine)  # clock time of job done
            machines_diary[machine] = time  # new time in diary

    machines = np.shape(jobs[0].time_on_machine)[0] # number of machines
    machines_diary = [0] * machines                 # array [t_1,t_2,t_machines] then job is done (new time)
    time=0
    machines_working = [0] * machines

    for job in queue:
        sim_time(jobs[job], machines_diary)

    return machines_diary[machines-1]  # the last done job


def neh(jobs):
    v_jobslist = []  # virtal jobs list (only 1 machine, time=time(0)+time(1)+...+time(n))
    for i in range(len(jobs)):
        sum = 0
        for j in range(jobs[i].size):
            sum = sum+jobs[i].time(j)
        v_jobslist.append([sum, len(jobs)-i])

    v_jobslist.sort(reverse=True)
    for i in range(len(v_jobslist)):
        v_jobslist[i][1] = (v_jobslist[i][1]-len(v_jobslist))*(-1)

    perm = []  # best queue
    perm.append(v_jobslist[0][1])  # first job (max time)
    cmaxlist = []
    perm_list = []
    tmp_perm = []  # temporary queue

    for k in range(len(perm)):
        tmp_perm.append(perm[k])  # tmp_perm=perm
    for i in range(1, len(v_jobslist)):
        for j in range(i+1):
            tmp_perm.insert(j, v_jobslist[i][1])  #a dd on position i
            # print(" PERM: ",tmp_perm, "CMAX: ", c_max(tmp_perm, jobs))
            cmaxlist.append(c_max(tmp_perm, jobs))  # and check time using cmax
            perm_list.append(tmp_perm)
            tmp_perm = []  #tmp_perm=perm
            for k in range(len(perm)):
                tmp_perm.append(perm[k])

        # Queue update!
        cmaxmin=cmaxlist[0]
        index = 0
        for j in range(1, len(cmaxlist)): # min(cmaxlist)
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


