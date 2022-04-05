# créer un jeu de math avec 4 questions aléatoire.

import random

NB_MIN = 1
NB_MAX = 10
NB_QUESTIONS = 4

# ici la fonction pose la question, si on laisse l'affichage de la réponse c'est
# un fonctionnement différent. du coup on met des boolen pour avoir vrai ou faux
def poser_question():
    a = random.randint(NB_MIN, NB_MAX)
    b = random.randint(NB_MIN, NB_MAX)
    c = random.randint(0,3)
    operation_str = "+"
    if c == 1:
        operation_str = "*"
    elif c == 2:
        operation_str = "-"
    elif c == 3:
        operation_str = "/"
    reponse_str = input(f"Combien font {a} {operation_str} {b} ?")
    reponse_int = int(reponse_str)
    calcul = a+b
    if c == 1:
        calcul = a*b
    elif c == 2:
        calcul = a-b
    elif c == 3:
        calcul = a/b
    if reponse_int == calcul:
        return True
    return False

# début code
nb_points = 0
for i in range (0, NB_QUESTIONS):
     print(f"Question {i+1} sur {NB_QUESTIONS}.")
     if poser_question():
      print("Bonne réponse !")
      nb_points +=1
     else:
        print("mauvaise réponse.")

print(f"Le test est terminé et votre score est de {nb_points}/{NB_QUESTIONS}.")
# Compliment sur le score + calcul moyenne
moyenne = int(NB_QUESTIONS/2)
if nb_points == NB_QUESTIONS:
    print("Excellent !")
elif nb_points == 0:
    print("Revisez vos maths.")
elif nb_points > moyenne:
    print("Vous êtes au dessus de la moyenne.")
else:
    print("Vous êtes en dessous de la moyenne.")
