from Fonctions import*
from os import *

def Matrices():
    system('cls')
    while True:
        # Menu :
        print(" #-----------------------------# Menu #-----------------------------#")
        print(" 1 ==> Addition de deux matrices A + B.")
        print(" 2 ==> Soustraction de deux matrices A - B.")
        print(" 3 ==> Multiplication de deux matrices A × B.")
        print(" 4 ==> Multiplication d'un nombre et une matrice αA.")
        print(" 5 ==> Puissance d'une matrice A^n.")
        print(" 6 ==> Détérminant d'une matrice Det(A).")
        print(" 7 ==> Matrice transposé de A.")
        print(" 8 ==> Comatrice de A.")
        print(" 9 ==> Matrice invérse de A.")
        print(" 0 ==> Quitter.")
        print(" #------------------------------------------------------------------#")
        choix = input(" Entrer votre choix : ")
        # les choix :
        if choix == '1' or choix == '2': # l'addition ou la soustraction de deux matrices :
            n = int(input(" Entrer le nombre des lignes de A et B   : "))
            p = int(input(" Entrer le nombre des colonnes de A et B : "))
            A = Creer_Matrice(n, p, 'A')
            B = Creer_Matrice(n, p, 'B')
            if choix == '1':
                print(" A + B :")
                Afficher(Addition_Soustration(A, B, n, p, '+'), n, p) # 'A + B':
            else:
                print(" A - B :")
                Afficher(Addition_Soustration(A, B, n, p, '-'), n, p) # 'A - B':

        elif choix == '3': # MULTIPLICATION DE DEUX MATRICES :
            nA = int(input(" Entrer le nombre des lignes de A   : "))
            pA = int(input(" Entrer le nombre des colonnes de A : "))
            nB = int(input(" Entrer le nombre des lignes de B   : "))
            pB = int(input(" Entrer le nombre des colonnes de B : "))
            if pA != nB: # SI NOMBRE DES COLONNES DE 'A' != NOMBRE DES COLONNES DE 'B':
                print(" # MATH ERREUR #")
            else: # SI NOMBRE DES COLONNES DE 'A' == NOMBE DES COLONNES DE 'B':
                A = Creer_Matrice(nA, pA, 'A')
                B = Creer_Matrice(nB, pB, 'B')
                print(" A × B :")
                Afficher(Multiplication_Matrice(A, B, nA, pB, pA), nA, pB) # 'A × B':

        elif choix == '4': # MULTIPLICATION DE 'α' et 'A':
            n = int(input(" Entrer le nombre des lignes de A   : "))
            p = int(input(" Entrer le nombre des colonnes de A : "))
            α = float(input(" Entrer le nombre α : "))
            A = Creer_Matrice(n, p, 'A')
            print(" αA :")
            Afficher(Multiplication_Nombre(A, n, p, α), n, p) # 'αA':

        elif choix == '5': # 'A' PUISSANCE 'N':
            n = int(input(" Entrer le format de A : "))
            N = int(input(" Entrer la puissance   : "))
            A = Creer_Matrice(n, n, 'A')
            print(" A^n :")
            Afficher(Puissance(A, N, n), n, n) # 'A^n':

        elif choix == '6': # DETERMINANT DE 'A':
            n = int(input(" Entrez le format de A : "))
            A = Creer_Matrice(n, n,'A')
            print(" Det(A) :",Determinant(A, n)) # det(A):

        elif choix == '7': # LA MATRICE TRANSPOSE DE 'A':
            n = int(input(" Entrer le nombre des lignes de A   : "))
            p = int(input(" Entrer le nombre des colonnes de A : "))
            A = Creer_Matrice(n, p, 'A')
            print(" A' :")
            Afficher(Transpose(A, n, p), p, n) # A':

        elif choix == '8': # COMATRICE DE 'A':
            n = int(input(" Entrer le format de la matrice A : "))
            A = Creer_Matrice(n, n, 'A')
            print(" Com(A) :")
            Afficher(Comatrice(A, n), n, n) # 'Com(A)':

        elif choix == '9': # 'A' PUISSANCE '-1':
            n = int(input(" Entrer le format de la matrice A : "))
            A = Creer_Matrice(n, n, 'A')
            A_in = Matrice_Inv(A,n)
            if A_in != None:
                print(" A PUISSANCE -1 :")
                Afficher(A_in, n, n)
            else:
                print(" A n'est pas invérsible.")

        elif choix == '0': # QUITTER:
            system('cls')
            break

        else: # si le choix est invalid
            system('cls')

        print(" #------------------------------------------------------------------#")
        system('PAUSE')
        system('cls')
