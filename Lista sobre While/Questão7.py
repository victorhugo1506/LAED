numero = int(input("Digite um número inteiro: "))

if numero == 0:
    digitos = 1
else:
    if numero < 0:
        numero = numero * -1

    digitos = 0

    while numero > 0:
        numero = numero // 10
        digitos += 1

print("Quantidade de dígitos:", digitos)
