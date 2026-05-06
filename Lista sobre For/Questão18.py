def encontrar_divisores(n):
    divisores = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(i)
    return divisores

numero = int(input("Digite um número para ver se é primo: "))

if(len(encontrar_divisores(numero)) == 2):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo, seus divisores são: {encontrar_divisores(numero)}")