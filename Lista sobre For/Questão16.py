numero1 = 1
numero2 = 1

n = int(input("Digite o numero de interações para a sequencia de Fibonacci: "))

for i in range (1, n + 1):
    print(numero1, end=" ")
    numero3 = numero1 + numero2
    numero1 = numero2   
    numero2 = numero3