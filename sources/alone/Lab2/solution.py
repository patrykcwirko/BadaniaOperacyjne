#Load jobs from file
jobs_list=jobs_load('./ta000.txt')

order=AlgJohn(jobs_list)
if order != 0:
    print('Alg John, time: ',c_max(order, jobs_list), '   order: ', order)
else:
    print('Alg John, incorrect data!')