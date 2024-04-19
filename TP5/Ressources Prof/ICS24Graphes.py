import ICS24Matrices as M
class cGraphes():
    def __init__(self):
        self.__dicoA = {}
        self.__matA = M.cMatrices()
        
    def afficherMat(self):
        self.__matA.afficher()
        
    def afficherDico(self):
        print(self.__dicoA)
    
    def setDico(self, pDico):
        self.__dicoA = pDico.copy()
    
    def genMatrice(self):
        self.__matA.initMat(len(self.__dicoA))
        self.__matA.afficher()
        for cle,val in self.__dicoA.items():
            for voisin in val:
                self.__matA.setVal(cle,voisin,1)
                
    def existeCheminN(self, pDebut, pFin, pN):
        
        self.genMatrice()
        matAN=M.cMatrices() #Matrice d'adjacence à la puissance N
        matAN.importer(self.__matA.exporter())
        if pN==1:
            valRen=self.__matA.getVal(pDebut,pFin)
        else:
            for i in range(pN-1):
                matAN=self.__matA.multiplier(matAN,False)
            
        