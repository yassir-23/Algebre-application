from os import *
from Fonctions import *

def Systemes():
    while True:
        system('cls')
        print(" #-----------------------------# Menu #-----------------------------#")
        print(" 1 ==> Système de n équations et n inconnus.")
        print(" 0 ==> Quitter.")
        print(" #------------------------------------------------------------------#")
        choix = input(" Entrer votre choix : ")

        if choix == '1':
            n = int(input(" Entrer le nombre n : "))
            print(" Entrer les coefficients : ")
            A = Matrice(n, n)
            print(" Entrer les nombres de la partie à droite : ")
            b = Matrice(n, 1)
            if n > 0:
                resultat(Multiplication_Matrice(Matrice_Inv(A, n), b, n, 1, n), n)
            else:
                print(" Le système n'est pas un système de Cramer")
            system('PAUSE')

        elif choix == '0':
            break
#------------------------------------------------------------------------------#

'''def Elimination_gauss(X, n):
    det = 1
    pivot = 0
    for i in range(n):
        if X[i][i] == 0:
            for j in range(n):
                if X[j][i] != 0:
                    X[i], X[j] = X[j], X[i]
                    pivot = X[i][i]
                    break
        if pivot != 0:
            for ligne in range(i, n):
                a = X[ligne][i]
                for j in range(i, n+1):
                    X[ligne][j] -= (a * X[i][j] / pivot)
        else:
            break
    Xn = []
    for i in range(n, 0, i-1):
        for j in range(n-1):
            if j = 0:
                x = X[n-1][n]
            x -= X[i][j]
        x /= X[i][n-1]
        X.append(x)'''
