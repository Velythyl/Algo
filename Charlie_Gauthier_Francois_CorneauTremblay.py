# IFT 2125 : Devoir 4
# Etudiant 1 : Charlie Gauthier 20105623
# Etudiant 2 : François Corneau-Tremblay 20101907

import numpy as np

# DO NOT write anything outside functions and main (except imports)
# DO NOT call main()
# DO NOT change the method names
# Please remove all the print functions used for debugging purposes
# Please change the filename according to your names
# Submit **only*** this file on Studium, NOT a .zip, NOT a full folder
# Remaining of the homework needs to be handed (in paper) before the demo.

def c_target(T):
    A = T[0]
    B = T[1]

    def a(i):
        return A[i - 1]

    def b(i):
        return B[i - 1]

    # Teste si m-chaine:
    for i in range(1, len(A) + 1):
        if a(i) >= i:
            return -1
        if b(i) >= i:
            return -1

    def tau(i):
        if i == 0:
            return 1
        else:
            return tau(a(i)) + tau(b(i))

    return tau(len(A))

def minimal_size_c(w):
    """
    On fait deux suppositions logiques dans cette implementation:

    1. Le tableau minimal est necessairement de longueur m plus petite ou egale a w (en fait assurement plus petit que
    cela, mais on ne veut pas y aller trop fort...). En effet, on le voit tout de suite: chaque valeur maximale a
    chaque indice augment la cible de 1. Donc, si a un tableau de longueur w dont toutes les valeurs sont maximales, on
    a necessairement quelque chose avec une trop grande cible.
    2. On doit commencer des plus grandes valeurs possibles aux indices vers les plus basses. En effet, on sait aussi
    que si les valeurs sont trop basses, elles "bypass" les valeurs entre l'indice de la valeur trop grande et l'indice
    qui est cette valeur (ouf, la phrase atroce). Aussi, si on commencait par 0 au lien du max, on aurait une logique un
    peu trouble: on commencerait par directement aller chercher dans les plus grands tableaux possibles au lieu des plus
    petits (encore une fois a cause qu'on sait que les valeurs doivent etre les plus grandes possibles).
    """

    if w < 2:
        return -1

    def iter(T, best_candidat):
        f = c_target(T)
        if len(best_candidat) <= len(T) or f > w:
            return -1
        if f == w:
            return T

        for i in reversed(range(0, len(T[0])+1)):
            for j in reversed(range(0, len(T[0]) + 1)):
                import copy
                Tc = copy.deepcopy(T)
                Tc[0].append(i)
                Tc[1].append(j)

                c = iter(Tc, best_candidat)
                if c != -1:
                    best_candidat = c
        return best_candidat

    return iter([[0], [0]], [w] * w)

# Your code will be tested using tests similar to these ones.
# Be sure that it does not yield any error and that the two given tests give "True".
if __name__=="__main__":
    pass
