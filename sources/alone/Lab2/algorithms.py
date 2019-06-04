from job import *


def c_max(queue, jobs=[Job]):
    """
    Simulate process
    :param queue: An order to simulate total time
    :param jobs:  list(Job) contains times on machines
    :return: Total Time
    """
    def sim_time(job, machines_diary):
        """
        Simulate job
        :param job: times on machines
        :param machines_diary: last done job on machines
        :return:
        """
        machines_list = range(0, np.shape(job.time_on_machine)[0])
        time = 0

        for machine in machines_list:
            delay = machines_diary[machine] - time  # job delay
            if delay < 0:
                delay = 0
            time = time + delay + job.time(machine)  # clock time of job done
            machines_diary[machine] = time  # new time in diary

    machines = np.shape(jobs[0].time_on_machine)[0] # number of machines
    machines_diary = [0] * machines                 # array [t_1,t_2,t_machines] then job is done (new time)
    time=0
    machines_working = [0] * machines

    for job in queue:
        sim_time(jobs[job], machines_diary)

    return machines_diary[machines-1] #the last done job


#Johnson's rule (two machines)
def AlgJohn2(jobs):
    #group 1 contains jobs which time(0)<time(1)
    #group 2 contains other jobs
    G1=[]
    G2=[]
    for i in range(len(jobs)):
        if jobs[i].time(0)<jobs[i].time(1):
            G1.append((jobs[i].time(0), jobs[i].time(1), i))
        else:
            G2.append((jobs[i].time(1),jobs[i].time(0), i))

    if len(G1):
        G1.sort() #asc
    if len(G2):
        G2.sort(reverse=True) #desc

    G=G1+G2
    ind=[]
    #optimal order
    for i in range(len(G)):
        ind.append(G[i][2])
    return ind

#Johnson's rule (three machines)
def AlgJohn3(jobs):
    #makes two virtual machines (time on vm0=time(0) + time(1); time on vm1=time(1)+time(2))
    virtual_jobs_list=[]
    for i in range(len(jobs)):
        virtual_jobs_list.append(Job([jobs[i].time(0)+jobs[i].time(1),jobs[i].time(1)+jobs[i].time(2)]))
    return AlgJohn2(virtual_jobs_list)

def AlgJohn(jobs):
    num=num_of_machines(jobs)
    if num == 0:
        return 0
    elif num==2:
        return AlgJohn2(jobs)
    elif num==3:
        return AlgJohn3(jobs)
    elif num>3:
        return AlgJohnk(jobs)
    else:
        return 0#-1


#Johnson's rule (k machines)
def AlgJohnk(jobs):
    if jobs[0].size==2:
        return AlgJohn2(jobs)
    else:
        virtual_jobs_list = []
        times=[]
        for i in range(len(jobs)):
            for j in range(jobs[i].size-1):
                times.append(jobs[i].time(j)+jobs[i].time(j+1))
            virtual_jobs_list.append(Job(times))
            times=[]
        return AlgJohnk(virtual_jobs_list)

def NEH(jobs):
    v_jobslist=[] # virtal jobs list (only 1 machine, time=time(0)+time(1)+...+time(n))
    for i in range(len(jobs)):
        sum=0
        for j in range(jobs[i].size):
            sum=sum+jobs[i].time(j)
        v_jobslist.append([sum, len(jobs)-i])


    v_jobslist.sort(reverse=True)
    for i in range (len(v_jobslist)):
        v_jobslist[i][1]=(v_jobslist[i][1]-len(v_jobslist))*(-1)


    perm=[] #best queue
    perm.append(v_jobslist[0][1]) #first job (max time)
    cmaxlist=[]
    perm_list=[]
    tmp_perm=[] #temporary queue

    for k in range(len(perm)):
        tmp_perm.append(perm[k]) #tmp_perm=perm
    for i in range(1, len(v_jobslist)):
        for j in range(i+1):
            tmp_perm.insert(j, v_jobslist[i][1]) #add on position i
            #print(" PERM: ",tmp_perm, "CMAX: ", c_max(tmp_perm, jobs))
            cmaxlist.append(c_max(tmp_perm, jobs)) #and check time using cmax
            perm_list.append(tmp_perm)
            tmp_perm=[] #tmp_perm=perm
            for k in range(len(perm)):
                tmp_perm.append(perm[k])

        #Queue update!
        cmaxmin=cmaxlist[0]
        index=0
        for j in range(1,len(cmaxlist)): #min(cmaxlist)
            if cmaxlist[j]<cmaxmin:
                cmaxmin=cmaxlist[j]
                index=j
        perm=perm_list[index] #and update...
        cmaxlist=[]
        perm_list=[]
        tmp_perm=[] #tmp_perm=perm
        for k in range(len(perm)):
            tmp_perm.append(perm[k])
    return perm

def cmax(perm, jobs):
    #array of end times (i-1 job on j-1 machine), now filled with 0
    Cd = [[0] * (jobs[0].size+2) for i in range(len(perm)+2)] #
    Cw = [[0] * (jobs[0].size+2) for i in range(len(perm)+2)]
   

    for j in range(1,jobs[0].size+1): #machine number+1
        for i in range(1,len(perm)+1): #job number+1
            Cd[i][j]=max(Cd[i][j-1], Cd[i-1][j])+jobs[perm[i-1]].time(j-1) #coming

    for j in range(jobs[0].size,0,-1): #machine number+1
        for i in range(len(perm),0,-1): #job number+1
            Cw[i][j]=max(Cw[i][j+1], Cw[i+1][j])+jobs[perm[i-1]].time(j-1) #outgoing

    return Cd,Cw

def bestperm(perm, index, jobs):
    Cd, Cw=cmax(perm, jobs)
    cmaxlist=[]
    times=[]
    td=[0]*(jobs[0].size+1)
    
    for i in range(len(perm)+1):
        for j in range(1,len(td)):
            td[j]=max(td[j-1], Cd[i][j])+jobs[index].time(j-1)
            times.append(td[j]+Cw[i+1][j])
        cmaxlist.append(max(times))
        times=[]
        td=[0]*(jobs[0].size+1)

    mintime=max(cmaxlist)
    ind=0
    for i in range(len(cmaxlist)): #looking for min cmax
        if cmaxlist[i]<mintime:
            mintime=cmaxlist[i]
            ind=i #and index of min cmax
            
    #print(cmaxlist,'   wstawiam ',index, ' na pozycje ', ind)
    perm.insert(ind,index) #new perm (+index on ind position)
    return perm

def QNEH(jobs):
    v_jobslist=[] # virtal jobs list (only 1 machine, time=time(0)+time(1)+...+time(n))
    for i in range(len(jobs)):
        sum=0
        for j in range(jobs[i].size):
            sum=sum+jobs[i].time(j)
        v_jobslist.append([sum, len(jobs)-i])


    v_jobslist.sort(reverse=True)
    for i in range (len(v_jobslist)):
        v_jobslist[i][1]=(v_jobslist[i][1]-len(v_jobslist))*(-1)

    
    perm=[] #best queue
    perm.append(v_jobslist[0][1]) #first job (max time)
    for i in range(1, len(v_jobslist)):
        perm=bestperm(perm, v_jobslist[i][1], jobs)
    return perm

def deljob(perm, jobs, last):
    Cd, Cw=cmax(perm, jobs)
    cmaxlist=[]
    t=[0]*(jobs[0].size+1)
    for i in range(len(perm)):
        for j in range(len(t)):
            t[j]=Cd[i][j]+Cw[i+2][j]
        cmaxlist.append([max(t),len(perm)-i])
        t=[0]*(jobs[0].size+1)

    cmaxlist.sort(reverse=True) #

    for i in range (len(cmaxlist)):
        cmaxlist[i][1]=(cmaxlist[i][1]-len(perm))*(-1)
        
    if cmaxlist[0][1]==last:
        ind=cmaxlist[1][1]
    else:
        ind=cmaxlist[0][1]
    num=perm.pop(ind)

    return perm, num
    
def mod4QNEH(jobs):
    v_jobslist=[] # virtal jobs list (only 1 machine, time=time(0)+time(1)+...+time(n))
    for i in range(len(jobs)):
        sum=0
        for j in range(jobs[i].size):
            sum=sum+jobs[i].time(j)
        v_jobslist.append([sum, len(jobs)-i])


    v_jobslist.sort(reverse=True)
    for i in range (len(v_jobslist)):
        v_jobslist[i][1]=(v_jobslist[i][1]-len(v_jobslist))*(-1)

    
    perm=[] #best queue
    perm.append(v_jobslist[0][1]) #first job (max time)
    for i in range(1, len(v_jobslist)):
        perm=bestperm(perm, v_jobslist[i][1], jobs)
        perm, num=deljob(perm, jobs, v_jobslist[i][1])
        perm=bestperm(perm, num, jobs)
    return perm


def CPM(perm, jobs):
    EF = [[0] * (jobs[0].size+2) for i in range(len(perm)+2)] #
    
    cp=[]
    
    for j in range(1,jobs[0].size+1): #machine number+1
        for i in range(1,len(perm)+1): #job number+1
            EF[i][j]=max(EF[i][j-1], EF[i-1][j])+jobs[perm[i-1]].time(j-1) #coming

    maxef=max(max(EF))

    LS = [[maxef] * (jobs[0].size+2) for i in range(len(perm)+2)] #
    for j in range(jobs[0].size,0,-1): #machine number+1
        for i in range(len(perm),0,-1): #job number+1
            LS[i][j]=min(LS[i][j+1], LS[i+1][j])-jobs[perm[i-1]].time(j-1) #outgoing
    for j in range(1,jobs[0].size+1):
        for i in range(1,len(perm)+1):
            if LS[i][j]+jobs[perm[i-1]].time(j-1)==EF[i][j]:
                cp.append([jobs[perm[i-1]].time(j-1), i-1, j-1])
    return cp
        

def mod1QNEH(jobs):
    v_jobslist=[] # virtal jobs list (only 1 machine, time=time(0)+time(1)+...+time(n))
    for i in range(len(jobs)):
        sum=0
        for j in range(jobs[i].size):
            sum=sum+jobs[i].time(j)
        v_jobslist.append([sum, len(jobs)-i])


    v_jobslist.sort(reverse=True)
    for i in range (len(v_jobslist)):
        v_jobslist[i][1]=(v_jobslist[i][1]-len(v_jobslist))*(-1)

    
    perm=[] #best queue
    perm.append(v_jobslist[0][1]) #first job (max time)
    for i in range(1, len(v_jobslist)):
        perm=bestperm(perm, v_jobslist[i][1], jobs)
        cp=CPM(perm, jobs)
        cp.sort(reverse=True)
        perm, num=deljob(perm, jobs, cp[0][1])
        perm=bestperm(perm, num, jobs)
    return perm

def mod2QNEH(jobs):
    v_jobslist=[] # virtal jobs list (only 1 machine, time=time(0)+time(1)+...+time(n))
    for i in range(len(jobs)):
        sum=0
        for j in range(jobs[i].size):
            sum=sum+jobs[i].time(j)
        v_jobslist.append([sum, len(jobs)-i])


    v_jobslist.sort(reverse=True)
    for i in range (len(v_jobslist)):
        v_jobslist[i][1]=(v_jobslist[i][1]-len(v_jobslist))*(-1)

    perm=[] #best queue
    perm.append(v_jobslist[0][1]) #first job (max time)
    for i in range(1, len(v_jobslist)):
        perm=bestperm(perm, v_jobslist[i][1], jobs)
        cp=CPM(perm, jobs)
        sum_cp = [0] * len(perm) #
        maxsum=0
        ind=0
        for i in range(len(perm)):
            sum_cp[cp[i][1]]+=cp[i][0]
        for i in range(len(sum_cp)):
            if maxsum<sum_cp[i]:
                maxsum=sum_cp[i]
                ind=i
                
        perm, num=deljob(perm, jobs, ind)
        perm=bestperm(perm, num, jobs)
    return perm

def mod3QNEH(jobs):
    v_jobslist=[] # virtal jobs list (only 1 machine, time=time(0)+time(1)+...+time(n))
    for i in range(len(jobs)):
        sum=0
        for j in range(jobs[i].size):
            sum=sum+jobs[i].time(j)
        v_jobslist.append([sum, len(jobs)-i])


    v_jobslist.sort(reverse=True)
    for i in range (len(v_jobslist)):
        v_jobslist[i][1]=(v_jobslist[i][1]-len(v_jobslist))*(-1)

    perm=[] #best queue
    perm.append(v_jobslist[0][1]) #first job (max time)
    for i in range(1, len(v_jobslist)):
        perm=bestperm(perm, v_jobslist[i][1], jobs)
        cp=CPM(perm, jobs)
        sum_cp = [0] * len(perm) #
        maxsum=0
        ind=0
        for i in range(len(perm)):
            sum_cp[cp[i][1]]+=1
        for i in range(len(sum_cp)):
            if maxsum<sum_cp[i]:
                maxsum=sum_cp[i]
                ind=i
                
        perm, num=deljob(perm, jobs, ind)
        perm=bestperm(perm, num, jobs)
    return perm





    
