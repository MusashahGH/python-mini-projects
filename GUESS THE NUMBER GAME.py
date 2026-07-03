# Mini Projects in Python
# Guess the Number

import random
target = random.randint(1,100) #build_in module to generate random numbers

while True:
    userNumber=input("Guess the Target or Quit(Q): ")
    if(userNumber=="Q"):
        break

    userNumber = int(userNumber)
    if(userNumber == target):
        print("Success : Correct Guess!")
        break
    elif(userNumber < target):
        print("your number is too Small.Take a bigger guess....")
    else:
        print("your number is too Big.Take a smaller guess....")

print("----GAME OVER----")


