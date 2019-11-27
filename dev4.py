# Charlie Gauthier 20105623
# François Corneau-Tremblay 20101907

def forward(T):
    A = T[0]
    B = T[1]

    def a(i):
        return A[i-1]

    def b(i):
        return B[i-1]

    # Teste si m-chaine:
    for i in range(1, len(A)+1):
        if a(i) >= i:
            return -1
        if b(i) >= i:
            return -1

    def tau(i):
        if i==0:
            return 1
        else:
            return tau(a(i))+tau(b(i))

    return tau(len(A))

print(forward([[0, 0, 1], [0,1,2]]))

def backward(tau):
    if tau < 2:
        return -1

    def iter(T, best_candidat):
        f = forward(T)
        if len(best_candidat) <= len(T) or f > tau:
            return -1
        if f == tau:
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

    return iter([[0], [0]], [tau]*tau)

print(backward(6))