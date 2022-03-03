notas=[]
alumnos=[]
n=int(input("Cuantos alumnos son?"))
for i in range(n):
    alumnos.append(input("Introduce el nombre del alumno: "))
    notas.append(input("Introduce la nota del alumno: "))
for i in range(3):
    print(notas[i],alumnos[i])
