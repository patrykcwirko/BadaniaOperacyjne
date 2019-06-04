from job import Job
import numpy as np


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

    machines = np.shape(jobs[0].time_on_machine)[0]  # number of machines
    machines_diary = [0] * machines                  # array [t_1,t_2,t_machines] then job is done (new time)
    time=0
    machines_working = [0] * machines

    for job in queue:
        sim_time(jobs[job], machines_diary)

    return machines_diary[machines-1] #the last done job


def cmax(perm, jobs):
    # array of end times (i-1 job on j-1 machine), now filled with 0
    Cd = [[0] * (jobs[0].size + 2) for i in range(len(perm) + 2)]  #
    Cw = [[0] * (jobs[0].size + 2) for i in range(len(perm) + 2)]

    for j in range(1, jobs[0].size + 1):  # machine number+1
        for i in range(1, len(perm) + 1):  # job number+1
            Cd[i][j] = max(Cd[i][j - 1], Cd[i - 1][j]) + jobs[perm[i - 1]].time(j - 1)  # coming

    for j in range(jobs[0].size, 0, -1):  # machine number+1
        for i in range(len(perm), 0, -1):  # job number+1
            Cw[i][j] = max(Cw[i][j + 1], Cw[i + 1][j]) + jobs[perm[i - 1]].time(j - 1)  # outgoing

    return Cd, Cw
