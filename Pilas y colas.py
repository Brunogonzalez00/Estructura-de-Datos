frutas=[]
frutas2=[]

frutas.append('Banana')
frutas.append('Uvas')
frutas.append('Mango')
frutas.append('Naranja')

for i in range(len(frutas)):
    primero= frutas.pop()
    frutas2.append(primero)
    
print(frutas2)