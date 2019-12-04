# IFT 2125 : Devoir 4
# Etudiant 1 :
# Etudiant 2 :

import numpy as np

# DO NOT write anything outside functions and main (except imports)
# DO NOT call main()
# DO NOT change the method names
# Please remove all the print functions used for debugging purposes
# Please change the filename according to your names
# Submit **only*** this file on Studium, NOT a .zip, NOT a full folder
# Remaining of the homework needs to be handed (in paper) before the demo.

def c_target(T):
    return -1

def minimal_size_c(w):
    # Input : integer w>=1
    # Output : chain of minimal size

    return [[0,0], [0,0]]

# Your code will be tested using tests similar to these ones.
# Be sure that it does not yield any error and that the two given tests give "True".
if __name__=="__main__":
    T1 = np.array([[0, 1, 2, 3, 4], [0, 1, 0, 2, 2]])
    T2 = np.array([[0, 0, 0, 0, 3], [0, 1, 2, 3, 4]])
    T3 = np.array([[0, 2, 2, 2], [0, 1, 2, 3]])
    T4 = np.array([[10], [0]])

    # Answers should be
    # 13, 9, -1, -1

    print("---------- 3 a) ---------------")
    print("T1", int( c_weight(T1) )==13)
    print("T2", int( c_weight(T2) )== 9)
    print("T3", int(c_weight(T3)) == -1)
    print("T4", int(c_weight(T4)) == -1)


    t1 = 4
    result1 = list([[0,1],[0,1]])

    print("---------- 3 b) ---------------")
    print(list(minimal_size_c(wt) )==result1)





