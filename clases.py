import os

print("Crear archivo")
print("=============")

clientes = 'clientes.txt'

archivo = open(clientes, 'w')
archivos.write("45654871 Gonzalez  Bruno    27/09/02")
archivos.write("66581231 Poppe     Ignacio  13/08/02")
archivos.write("56813364 Vaca      Nicolas  22/06/02")
archivos.write("34899782 Diaz      Camila   09/11/02")
archivos.write("38738845 Peña      Fabricio 27/12/02")

if clientes in os.listdir("."):
    print("Archivo creado en la ruta: \n\n\t{0}\{1}".format(os.getcwd(), clientes))
else:
    print("El archivo no fue creado!!!")
    
archivo = open(clientes, 'r')
contenido=archivo.read()
print(contenido)
archivo.close()
