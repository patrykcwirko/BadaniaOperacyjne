#
# Zawiera funkcje potrzebne do operacji z problemem
#

from Problem import *
import time as t

clock = 0  # clock

def mtime(opt='start'):
    global clock

    if opt == 'start':
        clock = t.time()

    if opt == 'stop':
        clock = t.time() - clock
        # print('Measured time:',clock,'s')
        return clock


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
        jobs_list = []
        lines = []

        '''Load NAME and PARAMETERS'''
        for line in f:
            lines.append(line)
        name = lines.pop(0)
        param = lines.pop(0).rstrip().split(' ')
        jobs = int(param[0])
        machines = int(param[1])
        del param
        """Load times"""
        for line in lines:
            if 'str' in line:
                break
            values = [int(i) for i in line.split()]
            jobs_list.append(values)
        problem = Problem(machines, jobs, jobs_list)
    return problem

# def losowanie

# Load jobs from file
# jobs_list=jobs_load('./ta/test.txt')
'''
#rozmiar=open("rozmiar.txt","w")
latex=open("latex.txt", "w")
'''
latex = open("latex.txt", "w")
plik = []
for i in range(50):  # Liczba plików w folderze ta, max 121
    if i < 10:
        nazwa = './ta/ta00' + str(i) + '.txt'
    elif i < 100:
        nazwa = './ta/ta0' + str(i) + '.txt'
    else:
        nazwa = './ta/ta' + str(i) + '.txt'
    plik.append(nazwa)

for i in range(len(plik)):
    print(plik[i])
    # Load jobs from file
    problem = jobs_load(plik[i])
    # print('Cmax = ' + str(c_max(problem)))
    mtime('start')
    Cmax = c_max(problem)
    time_neh = mtime('stop')
    if i < 10:
        nazwa = 'ta00' + str(i)
    elif i < 100:
        nazwa = 'ta0' + str(i)
    else:
        nazwa = 'ta' + str(i)

    latex.write("%s, &, %.3f, &, %d\n" % (nazwa, time_neh, Cmax))
latex.close()
