"""
SA algorithm
"""
from algorithm_cmax import c_max
from random import randint, random
from math import exp

k = 0

#  Stop criterion
#  k_max or t_min have to be equal to 0
k_max = 1000   #  max iterations
t_min = 0       #  minimal temp

mi = 0.99 # wsp schladziania


def sa(perm0, jobs,  t0):
    """
    SA algorithm
    :param perm0:
    :param jobs:
    :param t0:
    :return:
    """

    global k

    # Step 1 Initialization by parameters
    perm = perm0
    t = t0

    # Step 2 Generate move
    while True:
        #perm1 = swap(perm.copy())
        perm1 = insert(perm.copy())
        # Step 3 Apply or not apply move
        proba = move_proba(c_max(perm.copy(), jobs.copy()), c_max(perm1.copy(), jobs.copy()), t)
        if proba >= random():
            perm = perm1

        # Step 4 cool down
        t = cool1(t)    
        # t = cool2(t)

        # Step 5 Stop criterion
        # I
        if k_max > 0:
            if k == k_max or t <= 0:
                break
        if t_min > 0:
            if t <= t_min:
                break      
        else:
            k = k + 1
            continue
    return perm


def move_proba(c, c1, t):
    """
    Chance 0 to 1 of move perm <- perm'
    :param c: cmax(pi)
    :param c1: cmax(pi')
    :param t: time T
    :return:
    """
    if c1 >= c:
        return exp((c-c1)/t)
    else:
        return 1


def move_proba2(c, c1, t):
    """
    Chance 0 to 1 of move perm <- perm'
    :param c: cmax(pi)
    :param c1: cmax(pi')
    :param t: time T
    :return:
    """
    if c != c1:
        return exp((c-c1)/t)
    else:
        return 0


def move_proba3(c, c1, t):
    """
    Chance 0 to 1 of move perm <- perm'
    :param c: cmax(pi)
    :param c1: cmax(pi')
    :param t: time T
    :return:
    """

    return exp((c - c1) / t)


def swap(perm):
    """
    Change positions of 2 random elements
    :param perm: permutation (pi)
    :return:
    """
    p = perm
    x = randint(0, len(perm)-1)
    y = x
    while y == x:
        y = randint(0, len(perm)-1)
    p[x] = perm[y]
    p[y] = perm[x]
    return perm


def insert(perm=[]):
    """
    Insert rand element of permutation into random
    space and move others, by making space
    for this random element
    :param perm:
    :return: 
    """
    perm = list(perm)
    elem = randint(0, len(perm)-1)
    elem = perm.pop(elem) # random element
    place = randint(0, len(perm) - 1)
    perm.insert(place, elem)
    return perm


def cool1(t):
    """
    Cool down by mi*T
    :param t: time T
    :return:
    """
    global mi
    return mi*t


def cool2(t):
    """
    Cool down by iterable
    :param t: time T
    :return:
    """
    global k, k_max
    return t*(k/k_max)
