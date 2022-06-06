import random


print    ("----------------------------------------------------------------------------------------------")
print    ("                              A Game of Rock, Paper & Scissors                                ")
print    ("----------------------------------------------------------------------------------------------")


while True:
    userChoice = input('Choose an option "R" for "Rock", "P" for "Paper", "S" for "Scissors" or Q for "Quit":\n ')

    if not userChoice in ['R','P','S', 'Q']:
        print("Please choose a letter(R, P, S, Q)!:\n ")
        continue
    if userChoice != "exit":
        choices = ['R','P','S']
        opChoice = random.choice(choices)
        print("Player: " + (userChoice) + ":" + "" + "CPU: " + (opChoice) )

        if opChoice == str.upper(userChoice):
            print("Tie!")
            continue
        elif userChoice == 'R' and opChoice.upper() == 'S':
            print("Rock beats Scissors, You won!")
            break
        elif opChoice == 'R' and userChoice.upper() == 'S':
            print("Rock beats Scissors, You lost!")
            break
        elif userChoice == 'P' and opChoice.upper() == 'R':
            print("Paper beats Rock, You won!")
            break
        elif opChoice == 'P' and userChoice.upper() == 'R':
            print("Paper beats Rock, You lost!")
            break
        elif userChoice == 'S' and opChoice.upper() == 'P':
            print("Scissors beats Paper, You won!")
            break
        elif opChoice == 'S' and userChoice.upper() == 'P':
            print("Scissors beats Paper, You lost!")
            break
        elif userChoice == 'Q':
            print("Thank you for participating")
            break
    else:
        print("PLease read the rules of the Game")
        break