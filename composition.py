# -*- coding: utf-8 -*-

# Gauthier Charlie 20105623

# Nom/Name Prénom/Given name Matricule/Student ID
# Nom/Name Prénom/Given name Matricule/Student ID

# Compose deux mappings ensemble, de gauche a droite
def compose(m1, m2, *argv):
    def _c(m1, m2):
        return tuple([m2[m1[i] - 1] for i in range(len(m1))])

    comp = _c(m1, m2)
    for arg in argv:
        comp = _c(comp, arg)

    return comp


def number_unrep(num):
    number_undict = {
        'A': 10,
        'B': 11
    }

    if num in number_undict:
        return number_undict[num]
    else:
        return int(num)


def number_rep(num):
    number_dict = {
        10: 'A',
        11: 'B'
    }

    if num in number_dict:
        return number_dict[num]
    else:
        return str(num)


# Mappe une fonction en un int correspondant en utilisant le fait que la concatenation es fonctions est un chiffre en
# base len(fonction)
def number_hash(f):
    string = ""
    for num in f:
        string += number_rep(num - 1)

    return int(string, len(f))


# Retrouve la fonction correspondant a un int dans une certaine base
def number_unhash(number_hash, base):
    # Passe de la base 10 a la base "base"
    # loosely inspired de https://www.codevscolor.com/python-convert-decimal-ternarybase-3/
    def _to_base(num):
        q, r = divmod(num, base)  # On divise le nombre par base, et on garde le reste aussi.
        if q == 0:  # S'il n'y a pas de q (donc r rentre dans base)
            return number_rep(r)  # on retourne r
        else:  # Sinon,
            return _to_base(q) + number_rep(r)  # on retourne la base de q, + r

    temp = _to_base(number_hash)
    func = [number_unrep(char) + 1 for char in temp]

    while len(func) < base:
        func.insert(0, 1)

    return tuple(func)


# s, un set de mappings
# f, un mapping qu'on cherche dans <s>
def composition(s, f):
    if f in s:
        return True

    genned_comps = set()
    for func in s:
        genned_comps.add(number_hash(func))

    old_len = -1
    while old_len < len(genned_comps):
        old_len = len(genned_comps)
        to_add = set()

        print(old_len)

        for n1 in genned_comps:
            f1 = number_unhash(n1, len(f))  # f1 is the unhash of the hash of f1, which is n1.

            for n2 in genned_comps:
                comp = compose(f1, number_unhash(n2, len(f)))
                if comp == f:
                    return True

                comp_as_num = number_hash(comp)
                if comp_as_num in genned_comps or comp_as_num in to_add:
                    continue

                to_add.add(comp_as_num)
                print(old_len+len(to_add))
        genned_comps = genned_comps.union(to_add)

    return False

# s, un set de mappings
# f, un mapping qu'on cherche dans <s>
def composition2(s, f):
    if f in s:
        return True

    genned_comps = s
    old_len = -1
    while old_len < len(genned_comps):
        old_len = len(genned_comps)
        to_add = set()
        print(old_len)

        for f1 in genned_comps:
            for f2 in genned_comps:
                comp = compose(f1, f2)
                if comp == f:
                    return True
                if comp in genned_comps or comp in to_add:
                    continue

                print(old_len+len(to_add))
                to_add.add(comp)
        genned_comps = genned_comps.union(to_add)

    return False


# s, un set de mappings
# f, un mapping qu'on cherche dans <s>
def composition3(s,f):
    S = set()
    Sprim = s

    while S != Sprim:
        S = Sprim

        genned = set()
        for m1 in S:
            for m2 in S:
                comp = compose(m1, m2)
                if comp == f:
                    return True
                genned.add(comp)
                print(len(S)+len(genned))

        Sprim = Sprim.union(genned)

    return False

f11 = tuple([3, 1, 3, 4])  # 1->3 2->1 3->3 4->4
f12 = tuple([3, 4, 2, 1])  # tuples car une liste ne peut pas
s1 = set([f11, f12])  # servir d'élément d'un ensemble
f1 = tuple([1, 1, 1, 2])

f21 = tuple([3, 5, 4, 2, 6, 8, 1, 7])
f22 = tuple([1, 4, 3, 2, 5, 6, 7, 8])
s2 = set([f21, f22])
f2 = tuple([8, 7, 6, 5, 4, 3, 2, 1])

f31 = tuple([3, 3, 4, 4, 5, 5])
f32 = tuple([3, 4, 2, 1, 6, 6])
f33 = tuple([4, 4, 4, 4, 5, 5])
s3 = set([f31, f32, f33])
f3 = tuple([2, 1, 4, 3, 5, 5])

f41 = tuple([1, 2, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12])
f42 = tuple([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1])
f43 = tuple([2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
s4 = set([f41, f42, f43])
f4 = tuple([2, 1, 4, 3, 5, 7, 7, 7, 7, 7, 7, 7])

f51 = tuple([3, 3, 5, 5, 7, 7, 1, 1, 11, 12, 12, 1])
f52 = tuple([3, 3, 1, 1, 5, 5, 7, 7, 7, 4, 12, 11])
f53 = tuple([1, 1, 3, 3, 5, 5, 9, 7, 9, 9, 10, 12])
s5 = set([f51, f52, f53])
f5 = tuple([7, 7, 3, 3, 1, 1, 5, 5, 12, 11, 10, 4])

f61 = tuple([3, 4, 4, 2, 6, 8, 1, 7, 3])
f62 = tuple([4, 4, 4, 4, 4, 5, 5, 8, 1])
s6 = set([f61, f62])
f6 = tuple([2, 1, 4, 4, 5, 6, 8, 7, 3])

#print(compose(f52, f52, f51))
#print(compose(f51, f51, f51, f52))

#print(compose(f51, f51, f51, f52, f51, f51, f51, f51))

#print(compose(f51, f51, f51, f52, f53))

#print(composition(s1, f1))
#print(composition(s2, f2))
#print(composition(s3, f3))
#print(composition(s4, f4))
print(composition3(s5, f5))
#print(composition(s6, f6))
