"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

--- Bulls & Cows ---
author: Lukasz Orszulik
email: luki93@seznam.cz
discord: Lukasz Orszulik, wo0cash
"""

#TODO naimportuj potřebné knihovny a moduly
import random

#pomocné proměnné
sline = "-" * 50
game_on = True

#opakující se smyčka - hra
print("Hi there!")
while game_on:
    guesses = 0
    #TODO pozdrav
    print(sline + "\nI`ve generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
    print(sline)
    a_number = str(random.randint(1000, 9999))
    print(a_number)
    #TODO while smyčka hádání čísla
    while True:
        b_number = input("Enter a number: ")
        #podminky, hlidani aby byly cisla 4, nezacinala 0 a byly všechny numerické
        if not b_number.isnumeric():
            print("You must type only digits")
        elif len(b_number) != 4:
            print("The number must be 4 digits long")
        elif b_number[0] == "0":
            print("The first digit must be between 1 - 9")
        else:
            guesses = guesses + 1
            a_list = list(enumerate(a_number)) #vytvoření indexů pro čísla
            b_list = list(enumerate(b_number))
            #print(a_list)
            #print(b_list)

            cows = []
            bulls = []
            
            #budeme porovnávat 1. jestli jsou zadaná čísla na indexech -> bulls
            #a jestli se nacházi v čísle -> cows
            for index, cislo in b_list:
                if cislo ==  a_list[index][1]:
                    print("Bull")
                    bulls.append(cislo)
                else:
                    if cislo in a_number and cislo not in cows:
                        print("cow")
                        cows.append(cislo)
        
               
        print(bulls)
        print(cows)   
        if len(bulls) == 4:
            print(f"Correct, you've guessed the right number in {guesses} guesses!")
            if guesses < 4:
                print("That`s amazing")
            elif guesses < 7:
                print("Average score")
            else:
                print("Not so good...")
            break
        else:
            continue

    guessing = input("Do you want to play again? (y/n): ")
    if guessing == "y":
        game_on = True
    else:
        game_on = False
print(sline + "\nThank you for your game\nBye!\n" + sline)    


            
        
   

# TODO počítej čas jaký uplyne než hráč uhodne výsledek

# TODO zapiš do textového souboru prubeh hry - počet odhadu a cas
