import Graph as Graph


print("===========")
print("Python TP 5 - Graphes")
print("===========")

graphe = Graph.Graph(4)

dGrph = {}
dGrph[0] = [1, 2]
dGrph[1] = [3]
dGrph[2] = [1, 3]
dGrph[3] = [0]


for dbt in dGrph:
    for fin in dGrph[dbt]:
        graphe.ajouterArete(dbt, fin)

print("")
print("===========")
print("Degre du graph")
print("===========")
print("")

print(graphe.degreeMax())

print("")
print("===========")
print("Degre du sommet 1")
print("===========")
print("")

print(graphe.degree(1))

print("")
print("===========")
print("Sommets adjacents au sommet 0")
print("===========")
print("")

print(graphe.sommetsAdjacents(0))

print("")
print("===========")
print("Vérification si le graphe est connexe")
print("===========")
print("")

print(graphe.estConnexe())

print("")
print("===========")
print("Chemin entre 0 et 2")
print("===========")
print("")

print("La distance est de :", graphe.distance(0, 2))

print("")
print("===========")
print("Chemin entre 0 et 4")
print("===========")
print("")

print(graphe.cheminsAll())

print("")
print("===========")
print("Matrice d'adjacence pour les chemins de longueur 2")
print("===========")
print("")

print(graphe.matrice_adjacence_longueur_2())

print("")
print("===========")
print("Affichage de la matrice d'adjacence")
print("===========")
print("")

graphe.afficher()





