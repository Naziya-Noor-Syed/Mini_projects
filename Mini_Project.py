import random

target = random.randint(1,100)
while True:
    userChoice = input("Guess the target or Quit:")
    if(userChoice == "Q"):
        break
    userChoice = int(userChoice)
    if (userChoice == target):
        print("Correct Guess")
        break
    elif (userChoice < target):
        print("Your number was too small, guess more bigger")
    else:
        print("Your number was too big, guess more smaller")


print("--Game Over--")

