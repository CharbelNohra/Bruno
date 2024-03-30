# function for guessing number
import random
from random import randint
import pyttsx3
import sentences

engine = pyttsx3.init()
# rate
rate = engine.getProperty("rate")
engine.setProperty("rate", 113)
# volume
volume = engine.getProperty("volume")
engine.setProperty("volume", 1.0)
# voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


# function of speak
def speak(text):
    engine.say(text)
    engine.runAndWait()


def guessinggame():
    computer = random.randint(1, 10)
    player = int(input("enter a number between 1 and 10 >> "))
    if player == computer:
        print("you win")
        speak("you win")
    else:
        print("you are a looser :)")
        speak("you are looser :)")


# function for rock paper scissors
def rockpaperscissors():
    t = ["rock", "paper", "scissors"]
    computer = t[randint(0, 2)]
    player = input("rock, paper, scissors >>> ")

    if player == computer:
        speak("Tie")
        print("Tie")
        print(computer)
        speak(computer)

    elif player == "rock":
        if computer == "scissors":
            speak("You win")
            print("You win")
            print(computer)
            speak(computer)
        else:
            speak("You loose, :) ")
            print("You loose, :) ")
            print(computer)
            speak(computer)

    elif player == "paper":
        if computer == "rock":
            speak("You win")
            print("You win")
            print(computer)
            speak(computer)
        else:
            speak("You loose, :) ")
            print("You loose, :) ")
            print(computer)
            speak(computer)

    elif player == "scissors":
        if computer == "paper":
            speak("You win")
            print("You win")
            print(computer)
            speak(computer)
        else:
            speak("You loose, :) ")
            print("You loose, :) ")
            print(computer)
            speak(computer)

    else:
        speak("Not valid")
        print("Not valid")

    computer = t[randint(0, 2)]


# function for calculator
def calculator():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y

    for calcul in sentences.calcul:
        print(calcul)

    choice = input("enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            if num2 == 0:
                print("the division can not be done")
            else:
                print(num1, "/", num2, "=", divide(num1, num2))

    else:
        speak("invalid input")
        print("Invalid Input")
