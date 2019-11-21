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

# A et B deux ensembles de même grandeur triés du plus petit au plus grand
# On definit tableau A comme etant le tableau dont la fenetre "slide" vers le bas et B le tableau dont la fenetre
# monte vers le haut.
#
# L'algo fonctionne en bougeant la fenetre par laquelle on voit les tableaux de plus en plus vers leur mediane
# respective. Une fois la mediane de chaque tableau trouvee, le fait qu'ils sont tries nous assure que la mediane
# des deux tableaux ensemble sera celle en position 2 de la jointure entre les fenetres.
#
# (Definition de "fenetre": c'est la vue du tableau. Par exemple, une fenetre de 2 a 4 dans [0,1,2,3,4,5,6,7...]
# voudrait dire qu'on voit le tableau [2,3]. Nos fenetres sont definies par a_min et a_max et b_min et b_max.)
#
# La mediane trouvee definit la mediane comme etant l'element apres celui du milieu lorsque le tableau est de
# longueur paire, et celui du milieu exactement sinon.
def find_merged_median(A, B):
    def get_median(arr, lower, upper):  # La mediane est ici est definie comme l'element apres celui du milieu
        index = (lower+upper)//2        # lorsque la fenetre est de longueur paire
        return arr[index], index

    if len(A) < 3:  # Cas degenere
        A.extend(B)
        A = list(sorted(A))
        m, _ = get_median(A, lower=0, upper=len(A))
        return m

    a_min = b_min = 0   # initialement, les fenetres font toute la longueur des tableaux
    a_max = b_max = len(A)-1
    while (a_max - a_min) > 2:
        mA, a_index = get_median(A, a_min, a_max)
        mB, b_index = get_median(B, b_min, b_max)

        # On s'assure que A est toujours le tableau dont la fenetre glisse vers le bas.
        if mA < mB:
            a_max, b_max = b_max, a_max
            a_min, b_min = b_min, a_min
            a_index, b_index = b_index, a_index
            A, B = B, A

        # Clou de l'algo: on sait que les tableaux sont tries. Donc, si on glisse les fenetres vers la mediane
        # respective de chaque tableau, on sait qu'on s'approche de la vraie mediane, et donc lorsqu'on joignera les
        # deux fenetres pour former un nouveau tableau on aura la vraie mediane au bon endroit.
        a_max = a_index + 1
        # Si la grosseur des tableaux est paire, il faut ajuster la fenetre qui glisse vers le haut
        b_min = b_index - (1 if (b_max - b_min) % 2 == 0 else 0)

    merged = A[a_min:a_max]
    merged.extend(B[b_min:b_max])
    merged = list(sorted(merged))

    return merged[2]

while True:
    temp = list(sorted(list(range(2*2))))
    median = temp[(len(temp)-1)//2]

    random.shuffle(temp)

    splitter = len(temp) // 2

    a = list(sorted(temp[:splitter]))
    b = list(sorted(temp[splitter:]))

    print("calc")
    if find_merged_median(a, b) != median:
        exit()