import numpy as np

#------------------------------------------------------------------------------# MATRICES FONCTIONS :
def Creer_Matrice(n, p, x): # CREATRION DE LA MATRICE 'X':
    if n > 0 and p > 0: # SI LIGNES > 0 ET COLONNES > 0
        X = []
        print(f" # La matrice {x}({n},{p}) : ")
        for i in range(n): # LIGNES:
            lX = list(map(float, input(' ').split())) # LA SAISIE DE NOMBRES DE LA LIGNE 'i':
            X.append(lX) # LIGNES 'i' --> X(n,p):
        print(" ---------------------------------------------------------------------")
        return X # MATRICE 'X':
    else: # CAS DE LIGNES <= 0 OU COLONNES <= 0:
        print("\n # MATH ERREUR #")
#------------------------------------------------------------------------------#
def Addition_Soustration(X, Y, n, p, op): # 'X + Y' ou 'X - Y':
    Z = []
    for i in range(n):
        lZ = []
        for j in range(p):
            if op == '+':
                lZ.append(X[i][j] + Y[i][j])
            else:
                lZ.append(X[i][j] - Y[i][j])
        Z.append(lZ)
    return Z # pour retour la matrice 'A + B'.
#------------------------------------------------------------------------------#
def Multiplication_Matrice(X, Y, nA, pB, pn): # 'X × Y':
    Z = []
    for i in range(nA):
        LZ = []
        for j in range(pB):
            x = 0
            for a in range(pn):
                x += X[i][a] * Y[a][j]
            LZ.append(x)
        Z.append(LZ)
    return Z
#------------------------------------------------------------------------------#
def Multiplication_Nombre(X, n, p, a): # 'αX':
    for i in range(n):
        for j in range(p):
            X[i][j] *= a
    return X #'αX':
#------------------------------------------------------------------------------#
def Puissance(X, N, n): # 'X' PUISSANCE 'N':
    T = X.copy()
    i = 1
    while i < N: # PUISSANCES:
        T = Multiplication_Matrice(T, X, n, n, n) # 'X * X^i':
        i += 1
    return T # 'X^N':
#------------------------------------------------------------------------------#
def Transpose(X, n, p): # MATRICE TRANSPOSE DE 'X':
    T = []
    for i in range(p): # LIGNES:
        LT = []
        for j in range(n): # COLONNES:
            LT.append(X[j][i]) # 'xji' --> 'i':
        T.append(LT) # LIGNES 'i' DANS 'T':
    return T # X':
#------------------------------------------------------------------------------#
def Comatrice(Y, n): # fonction pour calculer le comatrice de 'Y'
    X = Y.copy()
    T = []
    for i in range(n): # LIGNES:
        LT = []
        for j in range(n): # COLONNES:
            M = [] # COFACTEUR DE LA PLACE (i,j):
            for x in range(n): # LIGNES:
                if x != i: # ELIMINATION DE LA LIGNE 'i':
                    L = [] # LIGNE 'x' DE 'Mij':
                    for y in range(n): # COLONNES:
                        if y != j: # ELIMINAION DE LA COLONNE 'j':
                            L.append(X[x][y])
                    M.append(L)
            LT.append(Determinant(M, n-1) * pow(-1, (i+j+2))) # det(Mij) * (-1)^(i+j):
        T.append(LT) # 'Mij' --> 'com(Y)':
    return T # T = COM(Y):
#------------------------------------------------------------------------------#
def Determinant(Y ,n): # DETERMINANT DE 'Y':
    X = Y.copy()
    det = np.linalg.det(X)
    return det # DETERMINANT(Y):
#------------------------------------------------------------------------------#
def Matrice_Inv(X,n):
    Com = Comatrice(X, n)
    d = Determinant(X,n)
    if d != 0:
        return Multiplication_Nombre(Transpose(Com, n, n), n, n, 1/d)
    else:
        return None
#------------------------------------------------------------------------------#
def Afficher(X, n, p): # MATRICE 'X':
    for i in range(n): # LIGNES:
        print(' ', end = '')
        for j in range(p): # COLONNES:
            print("{:.6f}".format(X[i][j]), end = '   ')
        print()
#------------------------------------------------------------------------------# POLYNÔMES FONCTIONS :
def Polynome(p):
    print(f" Entrer les coefficients de {p} : ", end = ''); P = list(map(float, input().split()))
    return P
#------------------------------------------------------------------------------#
def Afficher_Pol(P, n):
    puissance = n-1
    for i in P:
        if puissance != 0:
            print(f" {i}(x^{puissance})", end = ' +')
        else:
            print(' '+str(i))
        puissance -= 1
    print(" #------------------------------------------------------------------#")
#------------------------------------------------------------------------------#
def derivee(P, r):
    for i in range(r):
        x = 1 # puissance
        for j in range(len(P)):
            P[j] *= (len(P) - x)
            x += 1
        P.pop()
    return P
#------------------------------------------------------------------------------#
def Image(P, x):
    s = 0
    for i in range(len(P)):
        s += (P[i] * pow(x, len(P)-i-1))
    return s
#------------------------------------------------------------------------------#
def Multiplicite(P, a):
    compteur = 1
    P = derivee(P, 1)
    while not Image(P, a):
        P = derivee(P, 1)
        compteur += 1
    return compteur

#------------------------------------------------------------------------------# SYSTEMES DES EQUATIONS LINEAIRES FONCTIONS:
def Matrice(n, p): # CREATRION DES MATRICES:
    X = []
    for i in range(n): # LIGNES:
        print(f" LIGNE {i+1} :", end = '')
        lX = list(map(float, input(' ').split())) # LA SAISIE DE NOMBRES DE LA LIGNE 'i':
        X.append(lX)
    print(" #------------------------------------------------------------------#")
    return X
#------------------------------------------------------------------------------#
def resultat(X, n): # AFFICHER LES INCONNUS:
    print(" Résultat :")
    for i in range(n): # LIGNES:
        print(f" x{i+1} =", X[i][0])
    print(" #------------------------------------------------------------------#")
#------------------------------------------------------------------------------#
