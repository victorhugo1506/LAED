infimo = int(input("Digite o infimo do conjunto: \n"))
supremo = int(input("Digite o supremo do conjunto: \n"))
somatoriodoconjunto = 0

for i in range(infimo, supremo + 1):
    print(i)
    somatoriodoconjunto += i
    print("Somatório do conjunto:", somatoriodoconjunto)