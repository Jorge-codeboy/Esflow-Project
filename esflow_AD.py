from librarian import bookshelf1 as lb
import esflow_UI as ef_UI

class methodsAD:

    def loadFile(arreglo, archivo):
        try:
            # MISSING ELIMINATE SPACE
            arch = open(archivo, "r")
            for reg in arch.readlines():
                reg = reg[0:46]
                arreglo.append(reg)
            arch.close()
        except:
            er = "Error, archivo ["+archivo+"] inexistente ..."
            lb.error(er)

    def recordFile(arreglo, archivo):
        arch = open(archivo, "w")
        for reg in arreglo:
            arch.write(reg)
        arch.close()

    def checkUser(user, psw):
        user = user+(" "*(30-len(user)))
        bandera_existe = False
        posicion_arreglo = -1
        for reg in ef_UI.methodsUI.ar_users:
            if psw != "!":
                psw = psw + (" "*(15-len(psw)))
                # It is to 45 cause otherwiswe 46 takes the \n symbol
                if user == reg[0:30] and psw == reg[30:45]:
                    bandera_existe = True
                    posicion_arreglo = ef_UI.methodsUI.ar_users.index(reg)
                    break
            else:
                if user == reg[0:30]:
                    bandera_existe = True
                    posicion_arreglo = ef_UI.methodsUI.ar_users.index(reg)
                    break

        return(bandera_existe, posicion_arreglo)

ef_AD = methodsAD