import math
import random


def t(s, n):
    def iter(n):
        if n <= s:
            return n**2
        else:
            return 3*iter(math.ceil(n/2)) + 16*n

    return iter(n)

print(t(67, 2**6 + 1))

def test():
    temp = list(range(2*500))
    random.shuffle(temp)

    a = list(sorted(temp[:500]))
    b = list(sorted(temp[500:]))



    # A et B deux ensembles de même grandeur triés du plus petit au plus grand
    # On definit tableau A comme etant le tableau dont la fenetre "slide" vers le haut et B le tableau dont la fenetre
    # descend vers le bas.
    #
    # L'algo fonctionne en bougeant la fenetre par laquelle on voit les tableaux de plus en plus vers leur mediane
    # respective. Une fois la mediane de chaque tableau trouvee, le fait qu'ils sont tries nous assure que la mediane
    # des deux tableaux ensemble sera celle en position 2 de la jointure entre les fenetres.
    #
    # (Definition de "fenetre": c'est la vue du tableau. Par exemple, une fenetre de 2 a 4 dans [0,1,2,3,4,5,6,7...]
    # voudrait dire qu'on voit le tableau [2,3])
    def find_merged_median(A, B):
        def get_median(arr, lower, upper):  # La mediane
            index = (lower + upper) // 2
            return arr[index], index

        a_min = b_min = 0
        a_max = b_max = len(A)-1

        while (a_max - a_min) > 2 and (b_max - b_min) > 2:
            mA, a_index = get_median(A, a_min, a_max)
            mB, b_index = get_median(B, b_min, b_max)

            if mA < mB:
                a_max, b_max = b_max, a_max
                a_min, b_min = b_min, a_min
                a_index, b_index = b_index, a_index
                A, B = B, A

            if (b_max - b_min) % 2 == 0:    # S'assure que les deux tableaux seront de meme taille!
                b_index -= 1

            a_max = a_index + 1
            b_min = b_index

        merged = A[a_min:a_max]
        merged.extend(B[b_min:b_max])
        merged = list(sorted(merged))
        return merged[2]

    return find_merged_median(a,b)

while True:
    print("calc")
    if test() != 499:
        exit()