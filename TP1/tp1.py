# Chapitre 1 

import math as m
import matplotlib.pyplot as plt

# Considérons la fonction définie par f(x) = cos(x/2)

def f1(x):
    return m.cos(x/2)

def f2(x):
    return (-2*x+5)

# Représentation graphique de la fonction f

def courbe(pF,pDeb,pFin,pPas):
    abscisse = pDeb
    ordonnee = pF(abscisse)
    x = [abscisse]
    y = [ordonnee]
    while abscisse <= pFin:
        abscisse += pPas
        ordonnee = pF(abscisse)
        x.append(abscisse)
        y.append(ordonnee)
    plt.plot(x, y)
    plt.title("Courbe de la fonction f")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.show()

# I - Recherche par balayage

def balayage(pF,pDeb,pPas):
    x = pDeb
    while pF(pDeb)*pF(x) > 0:
        x += pPas
    print("\nRéponse par balayage : ", x)
    return x

# II - Recherche par dichotomie

def dichotomie(pF,pA,pB,pEpsilon):
    a = pA
    b = pB
    while b - a > pEpsilon:
        m = (a + b) / 2
        if pF(a)*pF(m) <= 0:
            b = m
        else:
            a = m
    print("\nRéponse par dichotomie : ", m)
    return m

# III - Recherche par la sécante

def secante(pF,pA,pB,pEpsilon):
    a = pA
    b = pB
    while abs(b - a) > pEpsilon:
        m = (a * pF(b) - b * pF(a)) / (pF(b) - pF(a))
        a = b
        b = m
    print("\nRéponse par la sécante : ", m)
    return m

# Fonction de calcul des racines d'un polynome

def racine(a,b,c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b - m.sqrt(delta))/(2*a)
        x2 = (-b + m.sqrt(delta))/(2*a)
        print("Racine 1 : ", x1)
        print("Racine 2 : ", x2)
        return x1,x2
    elif delta == 0:
        x = -b/(2*a)
        print("Racine : ", x)
        return x
    else:
        print("Pas de solution réelle")
        return "Pas de solution réelle"
