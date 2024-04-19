import math as m
import sys as sys
import tp1 as tp1

def menu():
    print("\n\nBienvenue dans le menu :")
    print("1. Calcul d'une racine d'un polynome")
    print("2. Calcul de plusieurs racines d'un polynome")
    print("3. Calcul d'aucune racine d'un polynome")
    print("4. Recherche par balayage")
    print("5. Recherche par dichotomie")
    print("6. Recherche par la sécante")
    print("7. Quitter")

def quitter():
    print("Au revoir !")
    sys.exit(0)

choix = 0
while choix != 7:
    menu()
    choix = int(input("Entrez le numéro de votre choix : "))

    if choix == 1:
        print("\nRacines du polynome 1 :")
        tp1.racine(1,-3,-4)
    elif choix == 2:
        print("\nRacines du polynome 2 :")
        tp1.racine(1,-2,1)
    elif choix == 3:
        print("\nRacines du polynome 3 :")
        tp1.racine(1,2,3)
    elif choix == 4:
        tp1.courbe(tp1.f1,0,2*m.pi,0.01)
        tp1.balayage(tp1.f1,0,0.01)
    elif choix == 5:
        tp1.courbe(tp1.f1,0,2*m.pi,0.01)
        tp1.dichotomie(tp1.f1,0,2*m.pi,0.01)
    elif choix == 6:
        tp1.courbe(tp1.f1,0,2*m.pi,0.01)
        tp1.secante(tp1.f1,0,2*m.pi,0.01)
    elif choix == 7:
        quitter()
    else:
        print("Choix invalide. Veuillez entrer un numéro valide.")


