#
# Zawiera opis problemu i narzędzia do ustalenia jego cech
#
import numpy as np
from Konfig import *

class Problem:
    """
    Jobs req times on every machine so:

    time_on_machines=[t1,t2,..,tn] for n machines

    """
    # Constructor of problem

    def __init__(self):
        self.machins = 0
        self.task = 0
        self.time = [[0] * self.machine for i in range(self.task)]
        self.Cmax = 0


def num_of_machines(jobs):
    # returns number of machines 0 if jobs list is empty and -1 if number of machines is different
    nmin = 0;
    nmax = 0;
    if len(jobs) > 0:
        nmin = nmax = jobs[0].size
        for i in range(1, len(jobs)):
            if jobs[i].size < nmin:
                nmin = jobs[i].size
            elif jobs[i].size > nmax:
                nmax = jobs[i].size
        if nmin == nmax:
            return nmin
        else:
            return 0
    else:
        return 0


def c_max(problem=Problem):
    """
    Simulate process
    :param queue: An order to simulate total time
    :param jobs:  list(Job) contains times on machines
    :return: Total Time
    """
    #TODO: podłączyć klase konfig
    v_C = [[0] * 600 for i in range(600)]
    print(problem.machins)
    for i in range(problem.machins):
        for j in range(problem.task):
            if v_C[i][j-1] < v_C[i-1][j]:
                v_C[i][j] = v_C[i-1][j] + problem.time[i][j]
            else:
                v_C[i][j] = v_C[i][j-1] + problem.time[i][j]
        print("test")
    return v_C[problem.machins][problem.task]
    # def sim_time(job, machines_diary):
    #     """
    #     Simulate job
    #     :param job: times on machines
    #     :param machines_diary: last done job on machines
    #     :return:
    #     """
    #     machines_list = range(0, np.shape(job.time_on_machine)[0])
    #     time = 0
    #
    #     for machine in machines_list:
    #         delay = machines_diary[machine] - time  # job delay
    #         if delay < 0:
    #             delay = 0
    #         time = time + delay + job.time(machine)  # clock time of job done
    #         machines_diary[machine] = time  # new time in diary
    #
    # machines = np.shape(jobs[0].time_on_machine)[0] # number of machines
    # machines_diary = [0] * machines                 # array [t_1,t_2,t_machines] then job is done (new time)
    # time=0
    # machines_working = [0] * machines
    #
    # for job in queue:
    #     sim_time(jobs[job], machines_diary)
    #
    # return machines_diary[machines-1]  # the last done job



