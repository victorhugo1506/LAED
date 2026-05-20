n1 = int(input("Digite o primeiro numero: \n"))
n2 = int(input("Digite o segundo numero: \n"))
aux = 0
somatoriodoconjunto = 0

if n1 < n2:
    for i in range(n1, n2 + 1):
        print(i)
        somatoriodoconjunto += i
        print("Somatório do conjunto:", somatoriodoconjunto)
elif n1 > n2:
    n2 = aux
    n2 = n1
    n1 = aux
    for i in range(n1, n2 + 1):
        print(i)
        somatoriodoconjunto += i
        print("Somatório do conjunto:", somatoriodoconjunto)