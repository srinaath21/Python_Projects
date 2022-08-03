#step-1 choose a random number between 1 to 100
#step-2 choose difficulty level - Easy / Hard
#step-3 check if the number is closer to the number chosen by the computer
#   step-3.1 : if the chosen number is 45 lets say and the input number is 20, this is too low as the difference is 25
#   step-3.2 : if the input number is 50 then the difference is 5 wich is too close
#   step-3.3 : if the input number is 55 then the difference is 10 which is close  
#step-4 if the number is equal to the number chosen by the computer then end the game

#set levels easy = 10 tries / hard = 5 tries
import random

print("""  _____   _    _   ______    _____    _____     _______   _    _   ______     _   _   _    _   __  __   ____    ______   _____  
  / ____| | |  | | |  ____|  / ____|  / ____|   |__   __| | |  | | |  ____|   | \ | | | |  | | |  \/  | |  _ \  |  ____| |  __ \ 
 | |  __  | |  | | | |__    | (___   | (___        | |    | |__| | | |__      |  \| | | |  | | | \  / | | |_) | | |__    | |__) |
 | | |_ | | |  | | |  __|    \___ \   \___ \       | |    |  __  | |  __|     | . ` | | |  | | | |\/| | |  _ <  |  __|   |  _  / 
 | |__| | | |__| | | |____   ____) |  ____) |      | |    | |  | | | |____    | |\  | | |__| | | |  | | | |_) | | |____  | | \ \ 
  \_____|  \____/  |______| |_____/  |_____/       |_|    |_|  |_| |______|   |_| \_|  \____/  |_|  |_| |____/  |______| |_|  \_\                                                                                                                                
""")
chances = 0
print("Welcome to the Guessing Game!")
print("Guess the number which is between 1 and 100")
com_choice = random.randint(1, 100)


difficulty = input("choose your difficulty level : 1 for EASY and 2 for HARD: ")
if difficulty == '1':
    chances = 10
elif difficulty == '2':
    chances = 5
else:
    print("WRONG CHOICE !!!")


while chances > 0:
    if chances == 0:
        print("OOPS... YOU DID NOT GUESS THE NUMBER CORRECTLY... BETTER LUCK NEXT TIME")
    
    print(f"YOU HAVE {chances} MORE CHANCES LEFT ")
    
    guess = int(input("Guess the number: "))
    if guess == com_choice:
        print("CONGRAGULATIONS!!! YOU FOUND THE CORRECT ANSWER!")
        break
    elif guess > com_choice:
        closeness = guess - com_choice
        if closeness <= 5:
            print("Very Close...")
        elif closeness > 5 and closeness <=10:
            print("Close...")
        else:
            print("Your guess is larger than the answer") 
        chances -= 1 
    elif guess < com_choice:
        closeness = com_choice - guess
        if closeness <= 5:
            print("Very Close...")
        elif closeness > 5 and closeness <=10:
            print("Close...")
        else:
            print("Your guess is smaller than the answer")
        chances -= 1
    
    