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

    def __init__(self, machins, task, time):
        self.machins = machins
        self.task = task
        self.time = time
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
    v_C = [[0] * 100 for i in range(100)]
    for i in range(problem.machins):
        for j in range(problem.task):
            if v_C[i+1][j] < v_C[i][j+1]:
                v_C[i+1][j+1] = v_C[i][j+1] + problem.time[j][i]
            else:
                v_C[i+1][j+1] = v_C[i+1][j] + problem.time[j][i]
    return v_C[problem.machins][problem.task]



