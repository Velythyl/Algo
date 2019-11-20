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
    def find_merged_median(A, B):
        def iter_mediam(arr, lower, upper):
            index = (lower + upper) // 2
            return arr[index], index

        a_min = b_min = 0
        a_max = b_max = len(A)-1

        while (a_max - a_min) >= 2 and (b_max - b_min) >= 2:
            mA, a_index = iter_mediam(A, a_min, a_max)
            mB, b_index = iter_mediam(B, b_min, b_max)

            if mA < mB:
                a_max, b_max = b_max, a_max
                a_min, b_min = b_min, a_min
                a_index, b_index = b_index, a_index
                A, B = B, A

            a_max = a_index + 1
            b_min = b_index

        #print(a_max - a_min)
        #print(b_max - b_min)
        b_min -= 1
        a_min += 1

        merged = A[a_min:a_max]
        merged.extend(B[b_min:b_max])
        merged = list(sorted(merged))
        def get_median(arr):
            return arr[math.floor(len(arr)/2)]

        print(merged)
        return get_median(merged)

    return find_merged_median(a,b)

while True:
    print("calc")
    if test() != 500:
        exit()