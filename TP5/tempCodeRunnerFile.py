class Graph(Matrice):
    def __init__(self, n):
        super().__init__(n)
        self.__n = n
        self.__matrice = [[0 for i in range(n)] for i in range(n)]