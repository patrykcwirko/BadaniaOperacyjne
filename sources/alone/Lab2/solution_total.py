from itertools import *
from algorithm_john import *
import time as t

clock=0#clock

def mtime(opt='start'):
    global clock

    if opt == 'start':
        clock =t.time()

    if opt =='stop':
        clock = t.time()-clock
        #print('Measured time:',clock,'s')
        return clock
    
#Load jobs from file
#jobs_list=jobs_load('./ta/test.txt')
'''
#rozmiar=open("rozmiar.txt","w")
latex=open("latex3.txt", "w")
'''
latex=open("latexmod.txt", "w")
plik=[]
for i in range(121):
    if i<10:
        nazwa='./ta/ta00'+str(i)+'.txt'
    elif i<100:
        nazwa='./ta/ta0'+str(i)+'.txt'
    else:
        nazwa='./ta/ta'+str(i)+'.txt'
    plik.append(nazwa)

for i in range(len(plik)):
    print(plik[i])
    #Load jobs from file
    jobs_list=jobs_load(plik[i])
    mtime('start')
    orderqneh=QNEH(jobs_list)
    time_qneh=mtime('stop')
    cmaxqneh=c_max(orderqneh, jobs_list)
    mtime('start')
    ordermod1qneh=mod1QNEH(jobs_list)
    time_mod1qneh=mtime('stop')
    cmaxmod1qneh=c_max(ordermod1qneh, jobs_list)
    mtime('start')
    ordermod2qneh=mod2QNEH(jobs_list)
    time_mod2qneh=mtime('stop')
    cmaxmod2qneh=c_max(ordermod2qneh, jobs_list)
    mtime('start')
    ordermod3qneh=mod3QNEH(jobs_list)
    time_mod3qneh=mtime('stop')
    cmaxmod3qneh=c_max(ordermod3qneh, jobs_list)
    mtime('start')
    ordermod4qneh=mod4QNEH(jobs_list)
    time_mod4qneh=mtime('stop')
    cmaxmod4qneh=c_max(ordermod4qneh, jobs_list)

    if i<10:
        nazwa='ta00'+str(i)
    elif i<100:
        nazwa='ta0'+str(i)
    else:
        nazwa='ta'+str(i)
    
    latex.write("%s, &, %.3f, &, %d,&, %.3f, &, %d,&, %.3f, &, %d,&, %.3f, &, %d ,&, %.3f, &, %d\n"%(nazwa,time_qneh,cmaxqneh, time_mod1qneh, cmaxmod1qneh, time_mod2qneh, cmaxmod2qneh, time_mod3qneh, cmaxmod3qneh, time_mod4qneh, cmaxmod4qneh  ))
latex.close()
'''

    mtime('start')
    orderjohn=AlgJohn(jobs_list)
    time_algjohn=mtime('stop')
    mtime('start')
    orderneh=NEH(jobs_list)
    time_neh=mtime('stop')

    mtime('start')
    orderqneh=QNEH(jobs_list)
    time_qneh=mtime('stop')
    if i<10:
        nazwa='ta00'+str(i)+'.txt'
    elif i<100:
        nazwa='ta0'+str(i)+'.txt'
    else:
        nazwa='ta'+str(i)+'.txt' 

    #cmaxj=c_max(orderjohn, jobs_list)
    #cmaxn=c_max(orderneh, jobs_list)
    #latex.write("%s ,&, %.3f ,&,%d,&, %.3f ,&,%d \n" %(nazwa, time_algjohn, cmaxj, time_neh, cmaxn))
    #latex.write("%.3f,&,%.3f \n" %(time_qneh, c_max(orderqneh,jobs_list)))
    n=len(jobs_list)
    m=jobs_list[0].size
    rozmiar.write("%d,%d \n" %(n,m))

latex.close()
#rozmiar.close()

'''
