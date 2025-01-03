
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
QUESTIONS = [{
        "question": "Que représente le symbole T, à l'envers?",
        "reponses": [
            "A - Médiatrice",
            "B - Perpendiculaire"
        ],
        "reponse_correcte": "B"
    },
    {
        'question': "Que représente le symbole  //?",
        'reponses': [
            "A - parallèle",
            "B - opposés"
        ],
        'reponse_correcte': "A"
    },
    {
        'question': "Que représente le symbole x?",
        'reponses': [
            "A -fois ",
            "B -plus"
        ],
        'reponse_correcte': "A"
    },
    {
        'question': "Quel est le calcul à faire en 1er dans 16 + 453 x 352?",
        'reponses': [
            "A - 453 x 352",
            "B - 16 + 453"
        ],
        'reponse_correcte': "A"
    }
]


def print_pythagore(text, time_sleep=SLEEP_BETWEEN_TEXT):
    print(Fore.GREEN + text + Style.RESET_ALL)
    time.sleep(time_sleep)


def input_pythagore(text):
    return input(Fore.GREEN+ text + "\n" + Style.RESET_ALL)



if __name__ == '__main__':
    print_pythagore(        "Bonjour, je m'appelle Pythagore, je vais vous interroger sur vos compétences en Mathématiques")
    name = input_pythagore("Comment t'appelles tu ?")
    print_pythagore("Bonjour " + name + ", nous allons tout de suite commencer !")
    
    nombre_de_reponses_justes = 0
    nombre_de_questions_posées = 0
    
    for question in QUESTIONS:
        print_pythagore(question["question"])
        for reponse in question["reponses"]:
            print_pythagore(reponse)
        reponse = input_pythagore("Quelle est ta réponse ?")
        if (reponse == question["reponse_correcte"]):
            print_pythagore("Bonne réponse")
            nombre_de_reponses_justes = nombre_de_reponses_justes + 1
        else:
            print_pythagore("Mauvaise réponse")
        nombre_de_questions_posées = nombre_de_questions_posées + 1




       
    print_pythagore("Bravo tu as répondu correctement à " + str(nombre_de_reponses_justes) + " questions sur " + str(nombre_de_questions_posées))


    

    





