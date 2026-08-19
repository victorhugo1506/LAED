N = 10
Q = [0] * N
frente = 0
fundo = 0


def enfileira(elem):
    global fundo
    if fundo == N:
        print("Erro: O vetor da fila encheu!")
        return
    Q[fundo] = elem
    fundo += 1


def desenfileira():
    global frente
    if frente == fundo:
        print("Erro: A fila está vazia!")
        return -1
    valor = Q[frente]
    frente += 1
    return valor