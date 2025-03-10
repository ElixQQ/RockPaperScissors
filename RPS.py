import random

loop = True

while loop == True:

    print(""" ____            _      ____                       
|  _ \ ___   ___| | __ |  _ \ __ _ _ __   ___ _ __ 
| |_) / _ \ / __| |/ / | |_) / _` | '_ \ / _ \ '__|
|  _ < (_) | (__|   <  |  __/ (_| | |_) |  __/ |   
|_|_\_\___/ \___|_|\_\ |_|   \__,_| .__/ \___|_|   
/ ___|  ___(_)___ ___  ___  _ __ _|_|              
\___ \ / __| / __/ __|/ _ \| '__/ __|              
 ___) | (__| \__ \__ \ (_) | |  \__ \              
|____/ \___|_|___/___/\___/|_|  |___/              
""")

    rpsList = ["Rock","Paper","Scissors"]

    pcselect = random.choice(rpsList)
  
    playerInput = input("\n1.Rock! \n2.Paper! \n3.Scissors! \n:")

    if playerInput == "1" and pcselect == "Rock":
        print(pcselect)
        print("Draw")
        againInput = int(input("\n1.Again\n2.Exit\n"))
        if againInput == 1:
            loop == True
        elif againInput == 2:
            loop = False

    elif playerInput == "1" and pcselect == "Paper":
        print(pcselect)
        print("You lose")
        againInput = int(input("\n1.Again\n2.Exit\n"))
        if againInput == 1:
            loop == True
        elif againInput == 2:
            loop = False

    elif playerInput == "1" and pcselect == "Scissors":
        print(pcselect)
        print("You win")
        againInput = int(input("\n1.Again\n2.Exit\n"))
        if againInput == 1:
            loop == True
        elif againInput == 2:
            loop = False

    elif playerInput == "2" and pcselect == "Rock":
        print(pcselect)
        print("You win")
        againInput = int(input("\n1.Again\n2.Exit\n"))
        if againInput == 1:
            loop == True
        elif againInput == 2:
            loop = False

    elif playerInput == "2" and pcselect == "Paper":
        print(pcselect)
        print("Draw")
        againInput = int(input("\n1.Again\n2.Exit\n"))
        if againInput == 1:
            loop == True
        elif againInput == 2:
            loop = False

    elif playerInput == "2" and pcselect == "Scissors":
        print(pcselect)
        print("You lose")
        againInput = int(input("\n1.Again\n2.Exit\n"))
        if againInput == 1:
            loop == True
        elif againInput == 2:
            loop = False

    elif playerInput == "3" and pcselect == "Rock":
        print(pcselect)
        print("You lose")
        againInput = int(input("\n1.Again\n2.Exit\n"))
        if againInput == 1:
            loop == True
        elif againInput == 2:
            loop = False

    elif playerInput == "3" and pcselect == "Paper":
        print(pcselect)
        print("You win")
        againInput = int(input("\n1.Again\n2.Exit\n"))
        if againInput == 1:
            loop == True
        elif againInput == 2:
            loop = False
    
    elif playerInput == "3" and pcselect == "Scissors":
        print(pcselect)
        print("You Draw")
        againInput = int(input("\n1.Again\n2.Exit\n"))
        if againInput == 1:
            loop == True
        elif againInput == 2:
            loop = False

    else:
        print("Invalid input please try again")