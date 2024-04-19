import Matrice as M

uneMatrice = M.Matrice(3)
print(uneMatrice)

matrice2 = uneMatrice.copy()
print(matrice2)

matrice3 = M.Matrice(3)
matrice3.setMatrice([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrice3)

matrice4 = M.Matrice(3)
matrice4.setMatrice([[1, 5, 0], [0, 5, 3], [0, 0, 9]])

print(matrice4.is_triang_sup())

print(matrice3.is_triang_inf())

print(matrice2.is_diag())

print(matrice3.trace())

print(matrice3.somme_Matrice(matrice4))

print(matrice3.produit_Matrice(matrice4))

print(matrice3.puissance_Matrice(2))