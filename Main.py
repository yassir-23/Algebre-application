from os import *
from time import *
from Matrices import *
from Systemes import *
from Polynomes import *

while True:
    system('cls')
    print(" #-----------------------------# Menu #-----------------------------#")
    print(" 1 ==> Calcul matriciel.")
    print(" 2 ==> Systéme d'équations linéaires.")
    print(" 3 ==> Polynômes.")
    print(" 0 ==> Quitter.")
    print(" #------------------------------------------------------------------#")
    choix = input(" Entrer votre choix : ")

    if choix == '1':
        Matrices()

    elif choix == '2':
        Systemes()

    elif choix == '3':
        Polynomes()

    elif choix == '4':
        pass

    elif choix == '0':
        quit()
