# Stone, Paper, Scissors Game

'''1 for stone
-1 for paper 
0 for scissors'''

'''import random

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
youDict = {"stone":1, "paper":-1, "scissors":0}
reverseDict = {1:"stone", -1:"paper", 0:"scissors"}

you = youDict.get(youstr)

print(f"you choose {reverseDict[you]}\ncomputer is choosing... {reverseDict[computer]}")

if (computer == you):
    print("It's a tie!")

else:
    if (computer == 1 and you == -1):
        print("You Loose! Computer wins!")
    
    elif(computer == 1 and you == 0):
        print("You Loose! Computer wins!")

    elif (computer == -1  and you == 1):
        print("You win! Computer Loose!")
    
    elif(computer == -1 and you == 0):
        print("You win! Computer Loose!")

    elif (computer == 0 and you == 1):
        print("You win! Computer Loose!")
    
    elif(computer == 0 and you == -1):
        print("You Loose! Computer wins!")

    else:
        print("Invalid input! Please enter stone, paper or scissors.")
 '''
