from random import randint

def randomNumber():
    return randint(1,100)

def greet():
    name = input("What's your name?")
    if name == "Tanner":
        print("That's my name, too!")
    else:
        print("Hello, ", name)
    print("I'm thinking of a number between 1 and 100")

def recordGuess():
    guess = int(input("What's your guess?"))
    return guess


def numberGame():
    number = randomNumber()

    greet()
    guess = recordGuess()

    while guess:
        if number == guess:
            print("Thats right, the number was ", number)
            break
        elif number > guess:
            print("Nope, higher")
        else:
            print("Nope, lower")
        guess = recordGuess()


numberGame()