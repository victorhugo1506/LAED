n1 = int(input("Digite o primeiro numero: \n"))
n2 = int(input("Digite o segundo numero: \n"))

somatoriodoconjunto = 0

if n1 > n2:
    n1, n2 = n2, n1

i = n1
while i <= n2:
    print(i)
    somatoriodoconjunto += i
    print("Somatório do conjunto:", somatoriodoconjunto)
    i += 1
