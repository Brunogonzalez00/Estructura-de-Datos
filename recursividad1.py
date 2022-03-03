def cuenta_regresiva(numero):
    numero-=1
    if numero > 0:
        time.sleep(1)
        print(numero)
        cuenta_regresiva(numero)
    else:
        time.sleep(1)
        print("Boooooooom!")
    print("Fin de la función", numero)

import time
numero=int(input("Ingrese numero de cuenta regresiva: "))
cuenta_regresiva(numero)