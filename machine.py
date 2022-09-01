import random
import time


def machine():
    x = random.randrange(1, 6)
    num = int(
        input(
            "Try the guess the number the machine will output.\nIf you get it right, you win.\nIf you get wrong, your system32 folder will be deleted :)\nTry to guess: "
        ))
    print(f"The machine thought about... {x}!")
    time.sleep(1)
    if num == x:
        print("You WIN! Another day you will have a computer!")
        print("Goodbye! :)")
        time.sleep(3)

    else:
        print("you lose. Deleting system32 folder...")
        time.sleep(2)
        print("System32 folder suscessfuly deleted!\nGood Luck!")
        time.sleep(3)


def menu():
    print("*" * 10, "Welcome to BEAT THE MACHINE!", "*" * 10)


menu()
machine()