"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Radek Sedláček
email: radek.sedlacek13@email.cz
discord: elvinek
"""

import random
oddelovac = "-----------------------------------------------"
tries = 0
print (f"""Hi there!"
{oddelovac}
I've generated a random 4 digit number for you.
Let's play bulls and cows game.
{oddelovac}""")

def num_gen() ->str:
    """
    Generates 4 digit number (num) which doesn't start with 0 and has no duplicate numbers.
    """ 
    num = str(random.randint(1,9))
    while len(num) < 4:
        num_plus = str(random.randint(0,9))
        if num_plus not in num:
            num += num_plus
    return num

def guess() ->str:
    """
    Let's player guess a number (num_player) and checks if the input is a 4 digit number that doesn't start with number 0.
    """
    global tries
    while True:
        duplicity = False
        num_player = input("Enter a number: ")
        if not num_player.isdigit():
            print (f"""That is not a number.
{oddelovac}""")
        elif len(num_player) < 4 or len(num_player) > 4:
            print (f"""Number has to have 4 digits!
{oddelovac}""")
        elif num_player[0] == "0":
            print (f"""First digit can't be 0!
{oddelovac}""")
        else:
            for number in num_player:
                count = num_player.count(number)
                if count > 1:
                    duplicity = True
                    continue
            if duplicity == True:
                print (f""" No duplicate digits in the number!
{oddelovac}""")
            else:
                tries +=1
                return num_player
    
def assessment (num: str, player_try: str):
    """
    This function checks similarity between generated number and player input. Provides feedback in cows and bulls and tracks number of player tries.
    Prints outcome. Bull - correct number in right position. Cow - correct number in wrong position.
    Also tells if the player won and shows number of tries.
    """
    position = 0
    cows = 0
    bulls = 0
    if player_try == num and tries == 1:
        print (f"Correct, you've guessed the right number in {tries} guess!")
    elif player_try == num and tries > 1:
        print (f"Correct, you've guessed the right number in {tries} guesses!")
    else:
        for number in player_try:
            if number == num[position]:
                bulls += 1
            elif number in num:
                cows += 1
            position += 1
        print (f"{bulls} bulls, {cows} cows")
        print (oddelovac)

def play ():
    """
    Start's the game.
    """
    num = num_gen()
    while True:
        player_try = guess()
        assessment (num, player_try)
        if player_try == num:
            break

play()