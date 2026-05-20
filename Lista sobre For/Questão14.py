produtorio = 1
zerofatorial = 1
numeroparaparar = int(input("Digite um numero para ver até ele ao quadrado: \n"))

if numeroparaparar == 0:
    print("%d! = %d", numeroparaparar, zerofatorial)
else:
    for i in range(1, numeroparaparar + 1):
        print(i)
        produtorio *= i
    print("%d! = %d", numeroparaparar, produtorio)
