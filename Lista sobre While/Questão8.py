somatorio = 0
numeroparasomar = 0
                            
while numeroparasomar >= 0:
    numeroparasomar = int(input("Digite um numero para ser somado e digite um valor negativo para parar: \n"))
    if numeroparasomar <= 0:
        print("Somatório:", somatorio)
        break
    somatorio += numeroparasomar
    print("Somatório:", somatorio)