texto = input("Insira uma frase: ")
posicao = texto.lower().find("a")

if posicao != -1:
    print(f"O caractere 'A' surge pela primeira vez na posição {posicao + 1}.")
else:
    print("O caractere 'A' não se encontra na frase inserida.")