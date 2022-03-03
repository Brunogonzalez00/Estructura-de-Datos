def factorial(n):
    if n>1:
        n=n*factorial(n-1)
    return n

n=int(input("Digite el numero a calcular: "))
print("El factorial es: ", factorial(n))