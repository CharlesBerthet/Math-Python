# TP 1 Python - Charles Berthet

Ce projet contient deux fichiers Python : `test.py` et `tp1.py`. Voici une brève explication de chacun de ces fichiers :

## test.py

Le fichier `test.py` est le fichier qui permet de tester les fonctions.

## tp1.py

Le fichier `tp1.py` est le fichier principal de ce projet. Il contient les différentes fonctions qui permettent de trouver la valeur `x` au moment ou `y` passe la barre des abscisses
informations supplémentaires sur son fonctionnement.

---

### Balayage

La méthode permet de rechercher la solution approchée de l’équation f(x) = 0 en balayant les valeurs et tester
toutes les valeurs possibles à la précision souhaitée.

### Dichotomie

La méthode recherche la solution dans un intervalle, puis réduit cet intervalle de moitié en fonction de celui qui renferme le 0. Il répétera l'opération pour trouver la valeur avec la précision indiquée.

### Sécante

La méthode de la sécante permet de trouver la solution en utilisant 2 points initaux puis génère une séquence de points qui convergent vers une solution en traçant une ligne entre deux points et en utilisant l'intersection de cette ligne avec l'axe des x comme prochain point.