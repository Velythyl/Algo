#-*- coding: utf-8 -*-

# Gauthier Charlie 20105623

# Compose deux mappings ensemble, de gauche a droite
def compose(m1, m2):
    return tuple([m2[m1[i]-1] for i in range(len(m1))])

# s, un set de mappings
# f, un mapping qu'on cherche dans <s>
# fonction basee sur l'algo d'appartenance de permutations stupide puisqu'il ne se base pas sur le fait que les tuples
# soient des permutations. https://studium.umontreal.ca/pluginfile.php/5018181/mod_resource/content/1/1intro.pdf page
# 36/42.
#
# Je l'ai un peu modifie: on remarque qu'il y a un seul endroit ou on genere de nouvelles compositions. On peut donc y
# tester directement si cette nouvelle composition est f, ce qui nous évite beaucoup de tours de boucles potentiels si
# on ne regardait qu'a la fin comme dans l'algo original.
#
# Pour pallier au fait qu'on ne regarde plus a la fin si f est dans S ou S', on teste si f est dans s des le debut de la
# fonction.
#
# Pour finir, on sait que f n'est pas dans S comme dans l'original: si on ne trouve pas f ET qu'on ne trouve plus de
# nouvelles compositions.
def composition(s,f):
    if f in s:
        return True

    S = set()   # S est le set de mappings qu'on a genere le dernier tour de boucle
    Sprim = s   # Spim est le set de mappings genere ce tour de boucle

    while S != Sprim:       # Tant qu'on ne trouve plus de nouvelles compositions
        S = Sprim           # On update S

        genned = set()      # On fait un set temporaire qui contient les compositions generees ce tour-ci
        for m1 in S:        # Pour chaque paire de fonction dans S, dans les deux ordres
            for m2 in S:
                comp = compose(m1, m2)  # On compose la paire
                if comp == f:           # Si la composition est f
                    return True         # On a true
                genned.add(comp)        # Sinon, on l'ajoute aux compositions generees

        Sprim = Sprim.union(genned) # Après toutes les compositions, on les ajoute au Sprim

    return False    # Si on a tout genere les compositions possibles, et qu'on a pas trouve f, False.

f11 = tuple([3, 1, 3, 4]) # 1->3 2->1 3->3 4->4
f12 = tuple([3, 4, 2, 1]) # tuples car une liste ne peut pas
s1 = set([f11,f12])       # servir d'élément d'un ensemble
f1 = tuple([1, 1, 1, 2])

f21 = tuple([3, 5, 4, 2, 6, 8, 1, 7])
f22 = tuple([1, 4, 3, 2, 5, 6, 7, 8])
s2 = set([f21,f22])
f2 = tuple([8, 7, 6, 5, 4, 3, 2, 1])

f31 = tuple([3, 3, 4, 4, 5, 5])
f32 = tuple([3, 4, 2, 1, 6, 6])
f33 = tuple([4, 4, 4, 4, 5, 5])
s3 = set([f31,f32,f33])
f3 = tuple([2, 1, 4, 3, 5, 5])

f41 = tuple([1, 2, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12])
f42 = tuple([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1])
f43 = tuple([2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
s4 = set([f41,f42,f43])
f4 = tuple([2, 1, 4, 3, 5, 7, 7, 7, 7, 7, 7, 7])

f51 = tuple([3, 3, 5, 5, 7, 7, 1, 1, 11, 12, 12, 1])
f52 = tuple([3, 3, 1, 1, 5, 5, 7, 7, 7, 4, 12, 11])
f53 = tuple([1, 1, 3, 3, 5, 5, 9, 7, 9, 9, 10, 12])
s5 = set([f51,f52,f53])
f5 = tuple([7, 7, 3, 3, 1, 1, 5, 5, 12, 11, 10, 4])

f61 = tuple([3, 4, 4, 2, 6, 8, 1, 7, 3])
f62 = tuple([4, 4, 4, 4, 4, 5, 5, 8, 1])
s6 = set([f61,f62])
f6 = tuple([2, 1, 4, 4, 5, 6, 8, 7, 3])

print(composition(s1,f1))
print(composition(s2,f2))
print(composition(s3,f3))
print(composition(s4,f4))
print(composition(s5,f5))
print(composition(s6,f6))