MAX = 100
pilha = []


def empilha(c):
    pilha.append(c)


def desempilha():
    return pilha.pop()


def pilha_vazia():
    return len(pilha) == 0


def inverter_palavras(string):
    resultado = ""
    for c in string + ' ':
        if c != ' ':
            empilha(c)
        else:
            while not pilha_vazia():
                resultado += desempilha()
            resultado += ' '
    return resultado.rstrip()


string = "ESTE EXERCICIO E MUITO FACIL"
print(f"Original:  {string}")
print(f"Invertida: {inverter_palavras(string)}")