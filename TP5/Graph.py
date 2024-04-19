from Matrice import Matrice

class Graph(Matrice):
    def __init__(self, n):
        super().__init__(n)
        self.__n = n
        self.__matrice = [[0 for i in range(n)] for i in range(n)]


    def __str__(self):
        return str(self.__matrice)


    def ajouterArete(self, dbt, fin):
        self.__matrice[dbt][fin] = 1


    def estAdjacent(self, dbt, fin):
        return self.__matrice[dbt][fin] == 1


    def nombreAretes(self):
        nbAretes = 0
        for i in range(self.__n):
            for j in range(i + 1, self.__n):
                if self.__matrice[i][j] == 1:
                    nbAretes += 1
        return nbAretes
    
    
    def degree(self, sommet):
        degree = 0
        for i in range(self.__n):
            if self.__matrice[sommet][i] == 1:
                degree += 1
        return degree
    

    def degreeMax(self):
        maxDegree = 0
        for i in range(self.__n):
            degree = 0
            for j in range(self.__n):
                if self.__matrice[i][j] == 1:
                    degree += 1
            if degree > maxDegree:
                maxDegree = degree
        return maxDegree
    

    def sommetsAdjacents(self, sommet):
        sommetsAdjacents = []
        for i in range(self.__n):
            if self.__matrice[sommet][i] == 1:
                sommetsAdjacents.append(i)
        return sommetsAdjacents
    

    def estConnexe(self):
        for i in range(self.__n):
            for j in range(self.__n):
                if self.__matrice[i][j] == 1:
                    return True
        return False


    def cheminslong2(self, sommet):
        chemins = []
        for sommetAdjacent in self.sommetsAdjacents(sommet):
            for sommetAdjacentAdjacent in self.sommetsAdjacents(sommetAdjacent):
                if sommetAdjacentAdjacent != sommet:
                    chemins.append([sommet, sommetAdjacent, sommetAdjacentAdjacent])
        return chemins


    def cheminsAll(self):
        for i in range(self.__n):
            print("Les chemins de longueur 2 pour le sommet", i, "sont :", self.cheminslong2(i))
        
    
    def distance(self, dbt, fin):
        if dbt == fin:
            return 0
        else:
            distance = 0
            sommets = [dbt]
            while fin not in sommets:
                sommetsSuivants = []
                for sommet in sommets:
                    for sommetAdjacent in self.sommetsAdjacents(sommet):
                        if sommetAdjacent not in sommetsSuivants:
                            sommetsSuivants.append(sommetAdjacent)
                sommets = sommetsSuivants
                distance += 1
            return distance


    def matrice_adjacence_longueur_2(graphe):
        matrice_longueur_2 = [[0 for _ in range(graphe.nb_sommets)] for _ in range(graphe.nb_sommets)]
        for i in range(graphe.nb_sommets):
            for j in range(graphe.nb_sommets):
                for k in range(graphe.nb_sommets):
                    matrice_longueur_2[i][j] += graphe.matrice_adjacence[i][k] * graphe.matrice_adjacence[k][j]
        return matrice_longueur_2
    



    def afficher(self):
        for ligne in self.__matrice:
            print(" ".join(map(str, ligne)))

    
    def afficher2(self):
        matrice2 = self.matrice2()
        for ligne in matrice2:
            print(" ".join(map(str, ligne)))

