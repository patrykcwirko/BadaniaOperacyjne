from itertools import *
from algorithm_sa import sa
import time as t
from job import jobs_load
from algorithm_neh import QNEH
from algorithm_cmax import c_max
import  numpy as np
clock = 0  # clock


def mtime(opt='start'):
    global clock

    if opt == 'start':
        clock = t.time()

    if opt == 'stop':
        clock = t.time() - clock
        # print('Measured time:',clock,'s')
        return clock


latex = open("latexmod.txt", "w")
plik = []
for i in range(120):
    if i < 10:
        nazwa = '../ta/ta00' + str(i) + '.txt'
    elif i < 100:
        nazwa = '../ta/ta0' + str(i) + '.txt'
    else:
        nazwa = '../ta/ta' + str(i) + '.txt'
    plik.append(nazwa)

for i in range(len(plik)):
    print(plik[i])
    # Load jobs from file
    jobs_list = jobs_load(plik[i])
    mtime('start')
    order_qneh = QNEH(jobs_list)
    time_qneh = mtime('stop')
    cmax_qneh = c_max(order_qneh, jobs_list)


    mtime('start')
    order = np.random.permutation(len(jobs_list))
    time_rand = mtime('stop')
    cmax_rand = c_max(order.copy(), jobs_list.copy())


    cmax_sa = 0
    time_sa = 0
    exps = 5
    for exp in range(exps):
        mtime('start')
        order_sa = sa(order, jobs_list, 1000)
        time_sa += mtime('stop')
        cmax_sa += c_max(order_sa.copy(), jobs_list.copy())
    cmax_sa /= exps
    time_sa /= exps


    cmax_sa_n = 0
    time_sa_n = 0
    for exp in range(exps):
        mtime('start')
        order_sa_n = sa(order_qneh.copy(), jobs_list.copy(), 1000)
        time_sa_n += mtime('stop')
        cmax_sa_n += c_max(order_sa_n.copy(), jobs_list.copy())
    cmax_sa_n /= exps
    time_sa_n /= exps



    if i < 10:
        nazwa = 'ta00' + str(i)
    elif i < 100:
        nazwa = 'ta0' + str(i)
    else:
        nazwa = 'ta' + str(i)

    latex.write("%s, &, %.3f, &, %d, &, %.3f, &, %d, &, %.3f, &, %.1f, &, %.3f, &, %.1f\n"%(nazwa,
                                                        time_qneh,  cmax_qneh,
                                                        time_rand,    cmax_rand,
                                                        time_sa, cmax_sa, # random order
                                                        time_sa_n, cmax_sa_n  # neh order
                                                        ))
latex.close()

