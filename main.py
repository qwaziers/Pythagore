
import logging.config
import re
import time
from colorama import Fore, Style, init

# from tools.envVariables import LOGGING_CONF_PATH
# logging.config.fileConfig(LOGGING_CONF_PATH)
# logger = logging.getLogger(__name__)

#init colorama to be able to print in color in the console
init(convert=True)

#clear the console at the beginning of the script
import os
os.system("cls" or "clear")



#defining global variables
SLEEP_BETWEEN_TEXT = 0


def print_pythagore(text, time_sleep=SLEEP_BETWEEN_TEXT):
    print(Fore.GREEN + text + Style.RESET_ALL)
    time.sleep(time_sleep)


def input_pythagore(text):
    return input(Fore.GREEN+ text + "\n" + Style.RESET_ALL)

def poser_question_une():
    print_pythagore("Que représente le symbole T, à l'envers?")
    print_pythagore("A - Médiatrice")
    print_pythagore("B - Perpendiculaire")
    reponse = input_pythagore("Quelle est ta réponse ?")
    if (reponse == "B"):
        print_pythagore("Bonne réponse")
        return "Correct"
    else:
        print_pythagore("Mauvaise réponse")
        return "Faux"
    

def poser_question_deux():
    print_pythagore("Que représente le symbole  //?")
    print_pythagore("A - parallèle")
    print_pythagore("B - opposés")
    reponse = input_pythagore("Quelle est ta réponse ?")
    if (reponse == "A"):
        print_pythagore("Bonne réponse")
        return "Correct"
    else:
        print_pythagore("Mauvaise réponse")
        return "Faux"
    
def poser_question_trois():
    print_pythagore("Que représente le symbole ?")
    print_pythagore("A - ")
    print_pythagore("B -")
    reponse = input_pythagore("Quelle est ta réponse ?")
    if (reponse == "A"):
        print_pythagore("Bonne réponse")
        return "Correct"
    else:
        print_pythagore("Mauvaise réponse")
        return "Faux"
    
if __name__ == '__main__':


    print_pythagore(        "Bonjour, je m'appelle Pythagore, je vais vous interroger sur vos compétences en Mathématiques")
    name = input_pythagore("Comment t'appelles tu ?")
    print_pythagore("Bonjour " + name + ", nous allons tout de suite commencer !")
    
    nombre_de_reponses_justes = 0
    nombre_de_questions_posées = 0
    
    resultat = poser_question_une()
    nombre_de_questions_posées = nombre_de_questions_posées + 1
    if (resultat == "Correct"):
        nombre_de_reponses_justes = nombre_de_reponses_justes + 1


    resultat = poser_question_deux()
    nombre_de_questions_posées = nombre_de_questions_posées + 1
    if (resultat == "Correct"):
        nombre_de_reponses_justes = nombre_de_reponses_justes + 1

    resultat = poser_question_trois()
    nombre_de_questions_posées = nombre_de_questions_posées + 1
    if (resultat == "Correct"):
        nombre_de_reponses_justes = nombre_de_reponses_justes + 1


    print_pythagore("Bravo tu as répondu correctement à " + str(nombre_de_reponses_justes) + " questions sur " + str(nombre_de_questions_posées))


    

    





