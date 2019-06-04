import numpy as np
import random
from operator import itemgetter, attrgetter, methodcaller


class Job:
    """
    Jobs req times on every machine so:

    time_on_machines=[t1,t2,..,tn] for n machines

    """
    # Constructor of jobe
    def __init__(self, time_on_machine):
        #array of times per machine
        self.time_on_machine = time_on_machine
        #how many times/machines Job contains
        self.size = np.shape(time_on_machine)[0]

    # Time on machine
    def time(self, machine):
        if machine < self.size:
            #time on specyfic machine
            return self.time_on_machine[machine]
        else:
            #time out of range
            print('Job time() size error')
            return None

def num_of_machines(jobs):
    #returns number of machines 0 if jobs list is empty and -1 if number of machines is different
    nmin=0;
    nmax=0;
    if(len(jobs)>0):
        nmin=nmax=jobs[0].size
        for i in range (1,len(jobs)):
            if jobs[i].size < nmin:
                nmin=jobs[i].size
            elif jobs[i].size > nmax:
                nmax=jobs[i].size
        if nmin == nmax:
            return nmin
        else:
            return 0
    else:
        return 0


def jobs_load(file_path='./ta000.txt'):
    """
    Load jobs from file.txt in format:
                    1 2 4
                    4 6 8
                    1 3 4
    :param file_path: path to .txt file
    :return: list(Job)
    """
    with open(file_path, 'r') as f:
        jobs_list=[]
        lines=[]

        '''Load NAME and PARAMETERS'''
        for line in f:
            lines.append(line)
        name=lines.pop(0)
        param=lines.pop(0).rstrip().split(' ')
        jobs=int(param[0])
        machines=int(param[1])
        del param
        """Load times"""
        for line in lines:
            if 'str' in line:
                break
            values = [int(i) for i in line.split()]
            jobs_list.append(Job(values))

    return jobs_list

def test_jobs(jobs, machines):
    jobs_list=[]
    times=[]
    for i in range(jobs):
        for j in range(machines):
            times.append(random.randint(1,30))
        jobs_list.append(Job(times))
        times=[]
    return jobs_list