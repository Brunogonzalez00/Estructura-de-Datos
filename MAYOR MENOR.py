def maximo(x,y):
    if(x>y):
        return x
    else:
        return y

def minimo(x,y):
    if(x<y):
        return x
    else:
        return y
    
x=int(input("Un numero: "))
y=int(input("Otro numero: "))
print("Maximo es: ", maximo(x,y),"El minimo es: ", minimo(x,y))