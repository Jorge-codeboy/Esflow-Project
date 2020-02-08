import os
from colorama import init
from termcolor import colored
from librarian import bookshelf1 as lb
import esflow_AD as ef_AD


class methodsUI:

    ar_users = []
    ar_reg = []

    def menu():
        op = -1
        while op != 3:
            os.system('cls')
            print('\U0001F4AA'+' ----¡Hola y Bienvenido a ESFLOW DIETS!---- ' +
                '\U0001F4AA')
            print('\n')
            print('---------------- M   E   N   U -------------------')
            print('1. Iniciar Sesión')
            print('2. Registrarse')
            print('3. Salir' + '\n')

            op = int(lb.ask_number('Introduzca su opción: ', 1, 3))
            ef_AD.methodsAD.loadFile(ef_UI.ar_users, "users.txt")

            if (op == 1):
                while True:
                    #os.system('cls')
                    user = lb.ask_string("Usuario: ", 2, 30)
                    psw = lb.ask_string("Constraseña: ", 5, 15)
                    flag, position = ef_AD.methodsAD.checkUser(user, psw)

                    if position == -1:
                        #os.system('cls')
                        lb.error("Usuario o contraseña incorrectos")
                    else:
                        lb.error("WELCOMW!!!!!!!")
                        break

            if (op == 2):
                # Asking for userName
                while True:
                    os.system('cls')
                    user = lb.ask_string("Usuario: ", 2, 30)
                    flag, position = ef_AD.methodsAD.checkUser(user, "!")
                # Checking in database
                    if position != -1:
                        lb.error("Usuario ya existente")
                    else:
                        psw = lb.ask_string("Constraseña: ", 5, 15)
                        ef_UI.ar_users.append(user+(" "*(30-len(user))) +
                                              psw + (" "*(15-len(psw))) + '\n')
                        ef_AD.methodsAD.recordFile(ef_UI.ar_users, "users.txt")
                        break


ef_UI = methodsUI()
