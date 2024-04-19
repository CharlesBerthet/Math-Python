class Matrice :
    def __init__(self, n) :
        self.__n = n
        self.__data = [[0 for i in range (n)] for i in range (n)]
    
    def __str__(self):
        return str(self.__data)
    
    def copy(self):
        m = Matrice(self.__n)
        for i in range(self.__n):
            for j in range(self.__n):
                m.__data[i][j] = self.__data[i][j]
        return m
    
    def setMatrice(self, data):
        self.__data = data

    def is_triang_sup(self):
        for i in range(self.__n):
            for j in range(i):
                if self.__data[i][j] != 0:
                    return False
        return True
    
    def is_triang_inf(self):
        for i in range(self.__n):
            for j in range(i+1, self.__n):
                if self.__data[i][j] != 0:
                    return False
        return True
    
    def is_diag(self):
        return self.is_triang_sup() and self.is_triang_inf()

    def trace(self):
        s = 0
        for i in range(self.__n):
            s += self.__data[i][i]
        return s
    
    def somme_Matrice(self, m):
        for i in range(self.__n):
            for j in range(self.__n):
                self.__data[i][j] += m.__data[i][j]
        return self
    
    def produit_Matrice(self, m):
        p = Matrice(self.__n)
        for i in range(self.__n):
            for j in range(self.__n):
                for k in range(self.__n):
                    p.__data[i][j] += self.__data[i][k] * m.__data[k][j]
        return p
    
    def puissance_Matrice(self, n):
        p = self.copy()
        for i in range(n-1):
            p = p.produit_Matrice(self)
        return p