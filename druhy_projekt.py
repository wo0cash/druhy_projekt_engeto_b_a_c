"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

--- Bulls & Cows ---
author: Lukasz Orszulik
email: luki93@seznam.cz
discord: Lukasz Orszulik, wo0cash
"""

#TODO naimportuj potřebné knnihovny a moduly
import random
import os

#pomocné proměnné
sline = "-" * 50
game_on = True

#opakující se smyčka - hra
print("Hi there!\n" + sline)
while game_on:
    #TODO pozdrav
    print("I`ve generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
    print(sline)
    a_number = random.randint(1000, 9999)
    print(a_number)
    #TODO while smyčka hádání čísla
    while True:
        (guess_number := input("Enter a number: "))
        #podminky, hlidani aby byly cisla 4, nezacinala 0 a byly všechny numerické
        if not guess_number.isnumeric():
            print("You must type only digits")
        elif len(guess_number) != 4:
            print("The number must be 4 digits long")
        elif guess_number[0] == "0":
            print("The first digit must be between 1 - 9")
        else:
            #TODO smyčka for bude iterovat hadane cislo a porovnavat s inputem uzivatele
            print("OK")
        
        
            break
    break

#TODO Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, 
# pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky

# TODO program vyhodnoti tip uzivatele - bull cisla na spravnem miste, cow - uhadnuta cisla ale na jiných pozicích

# TODO počítej čas jaký uplyne než hráč uhodne výsledek

# TODO zapiš do textového souboru prubeh hry - počet odhadu a cas
