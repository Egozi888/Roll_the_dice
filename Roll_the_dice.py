import random

def roll_the_dice():
    roll_res1 = random.randint(1, 6)
    return roll_res1  


def Guess_the_number():
    player1 = input("What is your name player 1?\n")
    player2 = input("What is your name player 2?\n")

    while True:
        try:
            player_guess1 = int(input(f"What is your choosen number {player1}\n?"))
            player_guess2 = int(input(f"What is your choosen number {player2}\n?"))
        except ValueError:
            print("not an integer")
            continue    
        roll1 = roll_the_dice()
        print(player1, "Rolled", roll1)
        roll2 = roll_the_dice()
        print(player2, "Rolled", roll2)
        if roll1 == player_guess1:
            print(player1, "Won")
            break
        elif roll2 == player_guess2:
            print(player2, "Won")
            break
        elif roll1 == player_guess1 == player_guess2 ==roll2:
            print(player1, "It's a TIE")
            break
        else:
            print("Let's try again")    
            continue



Guess_the_number()




