MAX = 100
fila = [0] * MAX
frente = 0
fundo = 0
qtd = 0


def enfileira(elem):
    global fundo, qtd
    fila[fundo] = elem
    fundo = (fundo + 1) % MAX
    qtd += 1


def desenfileira():
    global frente, qtd
    valor = fila[frente]
    frente = (frente + 1) % MAX
    qtd -= 1
    return valor


def excluir_negativos():
    if qtd == 0:
        return
    tamanho_original = qtd
    for _ in range(tamanho_original):
        valor = desenfileira()
        if valor >= 0:
            enfileira(valor)