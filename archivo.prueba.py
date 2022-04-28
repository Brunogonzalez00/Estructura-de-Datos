import os

print("\nCrear un archivo")
print("==================")

prueba = 'prueba.txt'

archivo = open(prueba, 'w')
archivo.write("El ciervo vive en los montes,\n el chivo en el corral, \n y el resto de los cornudos, \n con la mano en el celular.")
archivo.close()
