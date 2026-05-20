numeroparaparar = int(input("Digite um numero para ver até ele ao quadrado que não são multiplos de 4: \n"))
print("\n")

i = 1

while i <= numeroparaparar:
    j = i ** 2

    if j % 4 != 0:
        print(i)
        print("Ao quadrado:", j)

    i += 1
