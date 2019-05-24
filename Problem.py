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
    def __init__(self, machins = 0, task = 0, time = None ):
        self.machins = machins
        self.task = task
        self.time = [[0] * self.machine for i in range(self.task)] if time is None else time
        self.Cmax = 0
        self.perm = []


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



