# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 08:23:12 2024

@author: Userlocal
"""

# Exercice 1

# Avec liste d'adjacence
def degré(listesAdj):
    deg = 0
    for liste in listeAdj:
        if len(liste) > deg:
            deg = len(liste)
    return deg
            
# Avec dictionnaire

def degré2(dico):
    deg = 0
    for cle in dico.keys():
        if len(dico(cle)) > deg:
            deg = len(dico(cle))
    return deg

# Exercice 2

def accessibles(graphe,point):
    access  = graphe[point].copy()
    for x in access:
        liste = graphe[x]
        for y in liste:
            if y not in access:
                access.append(y)
    return access

# Test
graphe1 =  [[1,2,3],[0,2,4],[0,1,3,4],
 [0, 2, 5], [1, 2, 5,6],[3, 4,7],[4,7], [5, 6]]
                
print(accessibles(graphe1,7))

# Exercice 3

def isConnexe(graphe):
    test = True
    n = len(graphe)
    for i in range(n):
        for j in range(n):
            if (i not in accessibles(graphe,j) 
                and j not in accessibles(graphe,i)):
                test = False
    return test

print(isConnexe(graphe1))
       
# Obtenir la matrice d'adjacence à partir des listes d'adjacence         
def matriceAdj(listeAdj):
    n = len(listeAdj)
    mat = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in listeAdj[i]:
            mat[i][j] = 1
    return mat

# Exercice 4
#Un arbre est un graphe connexe tel que :
    # nb d'aretes = nb de sommets - 1

def nbAretes(graphe):
    # Le nb d'arêtes est la somme des degrés divisée par 2
    nb = 0
    for liste in graphe:
        nb += len(liste)
    return nb//2

def isArbre(graphe):
    if isConnexe(Arbre) and nbAretes(graphes) == len(graphe)-1:
        return True
    else:
        return False

        
        
            
            
            
            
            
            
            
            