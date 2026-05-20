infimo = int(input("Digite o infimo do conjunto: \n"))
supremo = int(input("Digite o supremo do conjunto: \n"))
somatoriodoconjunto = 0
i = infimo

while i <= supremo:
    print(i)
    somatoriodoconjunto += i
    print("Somatório do conjunto:", somatoriodoconjunto)
    i += 1