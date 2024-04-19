# Récursivité

# Exemple fonction factorielle

def factorielle1(n):
    if n == 0:
        valRen = 1
    else:
        valRen = factorielle1(n-1) * n
    return valRen


def factorielle2(n):
    if n == 0:
        return 1
    F = factorielle2(n-1) * n
    return F


def fZero(plnd,pLst):
    if plnd>=len(pLst):
        valRen = -1
    elif pLst[plnd] == 0:
        valRen = plnd
    else:
        valRen = fZero(plnd+1,pLst)
    return valRen


def fZeroV1M2(pLst):
    if pLst==[]:
        valRen=-1
    elif pLst[0]==0:
        valRen=0
    else:
        valRen=fZeroV1M2(pLst[1:])
        if valRen>=0:
            valRen+=1
        print(valRen)
        return valRen
    

def fZeroV1M3(pLst):
    if pLst==[]:
        valRen=-1
    elif pLst[-1]==0:
        valRen=len(pLst)-1
    else:
        valRen=fZeroV1M3(pLst[:-1])
        if valRen>=0:
            valRen-=1
    print(valRen)
    return valRen


def fZeroV1M4(pLst):
    if pLst==[]:
        valRen = 0
    else:
        long = len(pLst)
        valRen = 0
        for i in range(long):
            if pLst[i] == 0 :
                valRen += 1
    print(valRen)
    return valRen



# TP Python

from math import *
import matplotlib.pyplot as plt

# Exercice 1

def suite1(n):
    return log(1+1/n)

def suite2(n):
    return (3*exp(-1))**n

def suite3(n):
    return sqrt(n**2+1)-sqrt(n)

def graph():
    x = [i for i in range(1, 10)]
    y1 = [suite1(i) for i in x]
    y2 = [suite2(i) for i in x]
    y3 = [suite3(i) for i in x]
    plt.plot(x, y1, 'g*', label="log(1+1/n)")
    plt.plot(x, y2, 'cd', label="(3*exp(-1))**n")
    plt.plot(x, y3, 'm+', label="sqrt(n**2+1)-sqrt(n)")
    plt.legend()
    plt.show()


# Exercice 2 

def fonctionIterative1(n):
    u = 2
    for i in range(n):
        u = (1/3)*u + 1
    print(u)
    return u

def fonctionRecursive1(n):
    if n == 0:
        u = 2
    else:
        u = (1/3)*fonctionRecursive1(n-1) + 1
    print(u)
    return u


# Exercice 3

def fonctionIterative2(n):
    u = 1
    for i in range(n):
        u = u**2 / (sqrt(exp-u+2))
    print(u)
    return u

def fonctionRecursive2(n):
    u = 1
    if n == 0:
        u = 1
    else:
        u = fonctionRecursive2(n-1)**2 / (sqrt(exp-fonctionRecursive2(n-1)+2))
    print(u)
    return u


# Exercice 4

def fonctionIterative3(n):
    u = 2
    
    print(u)
    return u

def fonctionRecursive3(n):
    u = 2
    print(u)
    return u


# Exercice 5

