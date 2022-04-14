def estruct(n):
    m=0
    j=n-1
    for i in range (1,j,1):
        if(n%i==0):
            m=m+i
    return n

class PILA:
    def __init__(self):
        self.items=[]
    def añadir(self, x):
        self.items.append(x)
    def es_vacia(self):
        return self.items==[]
    def cantidad(self):
        return len(self.items)
    def imprimir(self):
        print(self.items)

pila=PILA()
m=0
op=4
while(op!=0):
    print("MENU")
    print("1) Añadir elementos")
    print("2) Cargar lista")
    print("3) Mostrar lista")
    print("0) Salir")
    op=int(input("\nSeleccione una opcion: "))
    if(op==1):
        n=int(input("Ingrese la cantidad de elementos"))
        for j in range(n):
            num=int(input("Ingrese numero"))
            pila.añadir(num)
    elif(op==2):
        for t in range(1,10,1):
            m=estruct(t)
            if(m!=0):
                pila.añadir(m)
    elif(op==3):
        print("Hay" ,pila.cantidad(),"de elementos en la lista")
        pila.imprimir()