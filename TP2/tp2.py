# Chapitre 2

import random as rd


# Exercice 1

def deNormal():
    lance = rd.randint(1,6)
    #print("Le lancé a donné : ", lance)
    return lance

def deTruque():
    des = [6, 6, 6, 6, 6, 5, 4, 3, 2, 1]
    lance = rd.choice(des)
    #print("Le lancé a donné : ", lance)
    return lance

def jetDe():
    x = rd.randint(1,4)
    if x <= 3:
        #print("Lancé normal")
        deNormal()
        return deNormal()
    else:
        #print("Lancé truqué")
        deTruque()
        return deTruque()

def nbr6():
    liste = [jetDe() for i in range(10000)]
    print("Nombre de 6 : ", liste.count(6))


# Exercice 2
    
def maxMin():
    liste = [deNormal() for i in range(10)]
    print("Maximum : ", max(liste))
    print("Minimum : ", min(liste))


# Exercice 3
    
def hasard():
    hsd = rd.randint(0,1)
    if hsd == 0:
        return -1
    else:
        return 1
    
def puce(n):
    abscisse = 0
    for i in range(n):
        abscisse += hasard()
    print("Position finale : ", abscisse)
    return abscisse

# Exercice 4
    
def jeu():
    nbr = rd.randint(1,100)
    trouve = False
    tentative = 0

    while trouve == False:
        proposition = int(input("Proposez un nombre : "))
        tentative += 1
        if proposition < nbr:
            print("Trop petit")
        elif proposition > nbr:
            print("Trop grand")
        else:
            print("Bravo, vous avez trouvé le nombre en ", tentative, "tentatives")
            trouve = True


# Exercice 5

def binomiale(n, p):



# Exercice 6

def lanceDe():

    nbr1, nbr2, nbr3, nbr4, nbr5, nbr6 = 0, 0, 0, 0, 0, 0

    for i in range(10):
        lance = deNormal()
        if lance == 1:
            nbr1 += 1
        elif lance == 2:
            nbr2 += 1
        elif lance == 3:
            nbr3 += 1
        elif lance == 4:
            nbr4 += 1
        elif lance == 5:
            nbr5 += 1
        elif lance == 6:
            nbr6 += 1

    print("Nombre de 1 : ", nbr1)
    print("Nombre de 2 : ", nbr2)
    print("Nombre de 3 : ", nbr3)
    print("Nombre de 4 : ", nbr4)
    print("Nombre de 5 : ", nbr5)
    print("Nombre de 6 : ", nbr6)      


# Exercice 7

def lance6():
    succes = False
    essais = 0
    while succes == False:
        lance = deNormal()
        essais += 1
        if lance == 6:
            succes = True
            print("Nombre d'essais : ", essais)  


# Exercice 8

def tirages():
    v = 30       
    r = 100      
    n = 0        
    for i in range(50):
        if rd.random() < v/(v+r):
            v = v-1
            n = n+1
        else:
            r = r-1
    return n
        
def moy_tirages(n):
    s = 0
    for i in range(n):
        s += tirages()
    return s/n

# Exercice 9

def grille():
    g = []
    for i in range(6):
        g += [int(input('entrer un numéro entre 1 et 49 : '))]
    return g

def loto():
    l = []
    urne = [k for k in range(1,50)] 
    for i in range(6):
        b = rd.randint(0,len(urne)-1)
        l += [urne[b]]
        urne.pop(b)                 
    return l
        
def jouer_loto():
    jeu = grille()
    tirage = loto()
    c = 0
    for i in range(6):
        if jeu[i] == tirage[i]:
            c = c+1
    print('vous avez ',c,' bon(s) numéro(s)')            



# Tirage de cartes
    
def tirage():

    # Déclaration du paquet de cartes
    paquet = {"coeur" : [1,2,3,4,5,6,7,8,9,10,11,12,13], "carreau" : [1,2,3,4,5,6,7,8,9,10,11,12,13], "pique" : [1,2,3,4,5,6,7,8,9,10,11,12,13], "trefle" : [1,2,3,4,5,6,7,8,9,10,11,12,13]}
    
    As = False

    # Boucle de tirage
    while As == False:
        couleur = rd.choice(list(paquet.keys()))
        carte = rd.choice(paquet[couleur])
        print("Carte tirée : ", carte, " de ", couleur)
        paquet[couleur].remove(carte)
        if carte == 1:
            As = True
            print("Un As a été tiré")


