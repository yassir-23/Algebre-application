import numpy as np
from Fonctions import  *
from os import *

def Polynomes():
    while True:
        system('cls')
        print(" #-----------------------------# Menu #-----------------------------#")
        print(" 1 ==> Division Euclidienne de deux polynômes.")
        print(" 2 ==> Dérivée d'ordre r d'un polynôme.")
        print(" 3 ==> Calcul de P(a).")
        print(" 4 ==> Multiplicité d'un racine.")
        print(" 0 ==> Quitter.")
        print(" #------------------------------------------------------------------#")
        choix = input(" Entrer votre choix : ")
        if choix == '1': # Division Euclidienne
            print(" Division Euclidienne de A(x)/B(x) :")
            A = Polynome('A(x)')
            B = Polynome('B(x)')
            quotient , retenue = np.polydiv(A, B) # Fonction qui retourne le quotient et le rest de la division euclidienne
            print(" #------------------------------------------------------------------#")
            print(" QUOTIENT :")
            print(" Q(x) =", end = '')
            Afficher_Pol(quotient, len(quotient))
            print(" REST :")
            print(" R(x) =", end = '')
            Afficher_Pol(retenue, len(retenue))
            system('PAUSE')

        elif choix == '2': # Dérivée d'ordre r d'un polynôme
            r = int(input(" Entrer l'ordre de la dérivé : "))
            P = Polynome('P(x)')
            if r >= 0:
                P = derivee(P, r)
                if r == 1:
                    mot = '-ére'
                else:
                    mot = '-éme'
                print(f" La {r}{mot} dérivée de P(x) :")
                print(" Q(x) =", end = '')
                Afficher_Pol(P, len(P))
            else:
                print(" Cette dérivée est négatif.")
            system('PAUSE')

        elif choix == '3':
            P = Polynome('P(x)')
            a = float(input(" Entrer a : "))
            print(f" P({a}) = {Image(P, a)}")
            system('PAUSE')

        elif choix == '4':
            P = Polynome('P(x)')
            a = float(input(" Entrer a : "))
            if not Image(P, a):
                print(f" La multiplicité de la racine {a} est {Multiplicite(P, a)}.")
            else:
                print(f" {a} n'est pas un racine de P.")
            system('PAUSE')

        elif choix == '0':
            break
