def encontrar_divisores(n):
    divisores = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(i)
    return divisores

numero = int(input("Digite um número para ver se é um primo clássico: "))

if numero < 1:
    print("Número inválido. Por favor, digite um número inteiro positivo.")
else:
    if(len(encontrar_divisores(numero)) == 2):
        print(f"{numero} é um número primo clássico.")
    else:
        print(f"{numero} não é um número primo clássico, seus divisores são: {encontrar_divisores(numero)}")