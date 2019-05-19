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
    jobs_list = jobs_load(plik[i])
    mtime('start')
    orderneh = neh(jobs_list)
    time_neh = mtime('stop')
    cmaxneh = c_max(orderneh, jobs_list)

    if i < 10:
        nazwa = 'ta00' + str(i)
    elif i < 100:
        nazwa = 'ta0' + str(i)
    else:
        nazwa = 'ta' + str(i)

    latex.write("%s, &, %.3f, &, %d\n" % (nazwa, time_neh, cmaxneh))
latex.close()


# def losowanie
