numeroparaparar = int(input("Digite um numero para ver até ele ao quadrado que não são multiplos de 4: \n"))

for i in range (1, numeroparaparar + 1):
    print(i)
    j = i**2
    if j % 4 == 0:
        continue
    print("Ao quadrado:", j)