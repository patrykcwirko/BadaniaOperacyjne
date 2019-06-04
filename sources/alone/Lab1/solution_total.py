from itertools import *
from algorithm_john import *
import time as t

clock=0#clock

def mtime(opt='start'):
    global clock

    if opt == 'start':
        #clock=time.time()
        clock =t.time()

    if opt =='stop':
        clock = t.time()-clock
        print('Measured time:',clock,'s')
        return clock

#Load jobs from file
jobs_list=jobs_load('./ta000.txt')

#List of jobs_index
jobs_queue = range(np.shape(jobs_list)[0])  # [0, 1, 2, n]
#Total permutation of jobs iterator
jobs_perm = permutations(jobs_queue) # [[1,2,3],[2,3,1]...]

Tmin=0

if num_of_machines(jobs_list) != 0:
    for comb in jobs_perm:    # for all combinations
        if Tmin == 0:
            Tmin=c_max(comb, jobs_list)
            order=comb
        else:
            time=c_max(comb, jobs_list)
            if Tmin > time:
                Tmin=time
                order=comb
        #print('Time of comb sim_ ', i, ':', sim_time_queue(comb, jobs_list))      #time of combination
        #print('Time of comb cmax ', i, ':', cmax(comb, jobs_list))      #time of combination

else:
    print('Cmax, incorrect data!')
if num_of_machines(jobs_list):
    print('cmax perm time: ',Tmin, '   order: ', order)
order=AlgJohn(jobs_list)
if order != 0:
    print('Alg John, time: ',c_max(order, jobs_list), '   order: ', order)
else:
    print('Alg John, incorrect data!')

#random jobs
num_machines=[2,3,4,5]
num_jobs=[2,3,5,10]
for k in range(len(num_machines)):
    for n in range(len(num_jobs)):
        print(num_jobs[n], 'jobs,  ', num_machines[k], 'machines ')
        jobs_list=test_jobs(num_jobs[n], num_machines[k])
        #for j in range(len(jobs_list)):
        #    for i in range (jobs_list[j].size):
       #         print(jobs_list[j].time(i),'&', end=' ')
        #    print('\\\\')

        #List of jobs_index
        jobs_queue = range(np.shape(jobs_list)[0])  # [0, 1, 2, n]

        #Total permutation of jobs
        jobs_perm = list(permutations(jobs_queue)) # [[1,2,3],[2,3,1]...]

        Tmin=0

        if num_of_machines(jobs_list) != 0:
            for comb in jobs_perm:    # for all combinations
                if Tmin == 0:
                    Tmin=c_max(comb, jobs_list)
                    order=comb
                else:
                    time=c_max(comb, jobs_list)
                    if Tmin > time:
                        Tmin=time
                        order=comb
                #print('Time of comb sim_ ', i, ':', sim_time_queue(comb, jobs_list))      #time of combination
                #print('Time of comb cmax ', i, ':', cmax(comb, jobs_list))      #time of combination

        else:
            print('Cmax, incorrect data!')

        if num_of_machines(jobs_list):
            print('cmax perm time: ',Tmin, '   order: ', order)
        order=AlgJohn(jobs_list)
        if order != 0:
            print('Alg John, time: ',c_max(order, jobs_list), '   order: ', order)
        else:
            print('Alg John, incorrect data!')