#
#Wyznacza najbardziej optymalna permutacje zadan problemu
#
from Problem import *
import random
import copy

def gen_pocz_pop(problem):
    for i in range(problem.task):
        problem.perm.append(i)

    popolacja = []
    for i in range(konfig.populacja):
        popolacja.append(copy.deepcopy(problem))

    for i in popolacja:
        random.shuffle(i.perm)
        for j in range(i.task):
            i.time[j] = problem.time[i.perm[j]]
        i.Cmax = c_max(i)

# def Reprodukcja():
#
# def krzyzowanie():
#
# def mutacja():

def evolution(problem):

    gen_pocz_pop(problem)
    
    # v_jobslist = []  # virtal jobs list (only 1 machine, time=time(0)+time(1)+...+time(n))
    # for i in range(len(jobs)):
    #     sum = 0
    #     for j in range(jobs[i].size):
    #         sum = sum+jobs[i].time(j)
    #     v_jobslist.append([sum, len(jobs)-i])
    #
    # v_jobslist.sort(reverse=True)
    # for i in range(len(v_jobslist)):
    #     v_jobslist[i][1] = (v_jobslist[i][1]-len(v_jobslist))*(-1)
    #
    # perm = []  # best queue
    # perm.append(v_jobslist[0][1])  # first job (max time)
    # cmaxlist = []
    # perm_list = []
    # tmp_perm = []  # temporary queue
    #
    # for k in range(len(perm)):
    #     tmp_perm.append(perm[k])  # tmp_perm=perm
    # for i in range(1, len(v_jobslist)):
    #     for j in range(i+1):
    #         tmp_perm.insert(j, v_jobslist[i][1])  #a dd on position i
    #         # print(" PERM: ",tmp_perm, "CMAX: ", c_max(tmp_perm, jobs))
    #         # cmaxlist.append(c_max(tmp_perm, jobs))  # and check time using cmax
    #         perm_list.append(tmp_perm)
    #         tmp_perm = []  #tmp_perm=perm
    #         for k in range(len(perm)):
    #             tmp_perm.append(perm[k])
    #
    #     # Queue update!
    #     cmaxmin=cmaxlist[0]
    #     index = 0
    #     for j in range(1, len(cmaxlist)): # min(cmaxlist)
    #         if cmaxlist[j] < cmaxmin:
    #             cmaxmin = cmaxlist[j]
    #             index = j
    #     perm = perm_list[index]  # and update...
    #     cmaxlist = []
    #     perm_list = []
    #     tmp_perm = []  # tmp_perm=perm
    #     for k in range(len(perm)):
    #         tmp_perm.append(perm[k])
    # return perm
