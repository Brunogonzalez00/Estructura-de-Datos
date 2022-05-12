def metersocio(socios):
    numero=int(input("Numero de socio(0 para cortar): "))
    while numero !=0:
        nombre=input("Nombre y apellido: ")
        fecha = input("Fecha de ingreso (DDMMAAAA):")
        cuota=input("Cuota diaria? s/n: ")
        socios[numero]=[nombre, fecha, cuota.lower()=="s"]
        numero =int(input("Numero de socio (0 para cortar): "))
    return socios

def fecha(socios, fechavieja, fechanueva):
    for datos in socios.values():
        if datos[1]==fechavieja:
            datos[1]=fechanueva
    return socios

def numerosocio(socios, nombre):
    for numero,datos in socios.items():
        if datos[0].lower()==nombre.lower():
            return numero
    return 0

def formatfecha(fecha):
    return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

def imprimirlista(socios):
    for numero,datos in socios.items():
        print("-Numero: ",numero)
        print("-Nombre: ",datos[0])
        print("-Ingreso: ",formatfecha(datos[1]))
        if datos[2]:
            print("-Cuota al dia")
        else:
            print("-Deudor")
            
sociosactivos={1:["Amanda Nuñez","17032009", True], 2:["Barbara Molina","17032009", True], 3:["Lautaro Campos","17032009", True]}
print("---Cargar socios")
sociosactivos=metersocio(sociosactivos)
print("El club tiene", len(sociosactivos), "socios")
print("-Registrar pago de cuotas")
numero=int(input("Numero de socio: "))
sociosactivos[numero][2]=True
print("-Modificando fecha de ingreso...")
sociosactivos=fecha(sociosactivos, "13032018","14032018")

x=input("Desea eliminar socio? (s/n): ")
if x=="s":
    print("-Eliminar socio")
    nombre=input("Nombre y Apellido :")
    numero=numerosocio(sociosactivos,nombre)
    if numero in sociosactivos:
        del sociosactivos[numero]
    imprimirlista(sociosactivos)
else:
    imprimirlista(sociosactivos)