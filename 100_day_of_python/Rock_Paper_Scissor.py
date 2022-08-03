# ROCK PAPER SCISSORS 

import random

choice = int(input("enter\n0 for R O C K\n1 for P A P E R\n2 for S C I S S O R\n"))
val = ["ROCK", "PAPER", "SCISSOR"]
com_choice = random.randint(0,2)
print(f"You chose {val[choice]}")
print(f"Computer chose {val[com_choice]}")
if (choice == 0 and com_choice == 1) or (choice == 1 and com_choice == 2) or (choice == 2 and com_choice == 0):
    print("You Lose !")
elif choice == com_choice:
    print("Match Draw. Try Again.")
else :
    print("You Win !")