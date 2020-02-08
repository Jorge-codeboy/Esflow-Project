# USE COLORS
# --1. Install colorama and termcolor with pip3
# from colorama import init
# from termcolor import colored
# --2. Then use Termcolor for all colored text output, must use
# --all 3 parameters, for black write grey
# print(colored('Hello, World!', 'grey', 'on_red'))
# --https://pypi.org/project/termcolor/
import os


class bookshelf1():
    # MAKE A PAUSE WITH A SPECIFIED MESSAGE
    def end():
        print("===================")
        input("=Coded by BabyLoco=")
        print()

    # MAKE A PAUSE WITH A SPECIFIED MESSAGE
    def error(message):
        print(message)
        input("[ENTER to continue]")

    # ASK FOR A STRING BETWEEN A RANGE OF CHARACTERS [INCLUSIVE]
    def ask_string(message, minimum, maximum):
        lenght = minimum - 1
        while lenght < minimum or lenght > maximum:
            print(message, end="")
            value = input("\n > ")
            length = len(value)
            if length < minimum or length > maximum:
                text = (
                    "Error, chain must be between "
                    + str(minimum)
                    + " y "
                    + str(maximum)
                    + " ...")
                bookshelf1.error(text)
                os.system('cls')
            else:
                break
        return str(value)

    # ASK FOR A NUMBER BETWEEN A RANGE [INCLUSIVE] RETURN A FLOAT
    def ask_number(message, minimum, maximum):
        value = minimum - 1
        while value < minimum or value > maximum:
            print(message, end="")
            value = float(input("\n > "))
            if value < minimum or value > maximum:
                text = (
                    "Error, number must be between "
                    + str(minimum)
                    + " y "
                    + str(maximum)
                    + " ...")
                bookshelf1.error(text)
                print('\r')
            else:
                break
        return value

    # RETURNS THE SUM OF FROM THE GIVEN NUMBER TO 1
    def summation(number):
        s = 0
        for i in range(1, number + 1):
            s = s + i
        return s

    # PENDING TO CREATE THE FUNCTION
    def prime_numbers(inferior, superior):
        for i in range(inferior, superior + 1):
            for c in range(1, i):
                if (i % c == 0 and c != i and c != 1):
                    break
                else:
                    print(i)

    # SOLVE INTEGRALS BY USING TRAPEZOID, FIRST YOU NEED fn FUNCTION
    def trapezoidIntegration(function, a, b, n):
        base = (b-a) / n
        halfBase = base / 2
        totalIntegration = 0
        for i in range(0, n):
            totalIntegration = (
                (totalIntegration) + (function((i - 1) * base + halfBase) + (
                    function(i * base + halfBase))) / 2)
        print("Trapezoid test!")
        print(">", totalIntegration * base)

        return (totalIntegration * base)

    # GET A LINE GIVEN TWO POINTS
    # IF YOU NEED TO INSERT MORE ADVANCED PARAMETERS, QUIT ASK NUMBER AND
    # ASSIGN DIRECTLY THE COORDINATES WITH AID OF MATH LIBRARY
    # REMEMEBER TO COVERT TO FLOAT THE INPUT FOR ACCURACY
    def equation_given2p(x1, y1, x2, y2):
        m = (y2-y1) / (x2-x1)
        print("-------------------------------------------------------------")
        print("The equation is y = " + str(m) + "x" + " + " + str((-m*x1)+y1))
