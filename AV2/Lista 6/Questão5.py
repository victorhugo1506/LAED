class Pilha:
    def __init__(self):
        self.itens = []

    def empilha(self, valor):
        self.itens.append(valor)

    def desempilha(self):
        return self.itens.pop()

    def vazia(self):
        return len(self.itens) == 0


def inverter_pilha(p):
    aux1 = Pilha()
    aux2 = Pilha()
    while not p.vazia():
        aux1.empilha(p.desempilha())
    while not aux1.vazia():
        aux2.empilha(aux1.desempilha())
    while not aux2.vazia():
        p.empilha(aux2.desempilha())


def verifica_palindromo(p):
    aux = Pilha()
    original = []

    while not p.vazia():
        letra = p.desempilha()
        original.append(letra)
        aux.empilha(letra)

    for letra in original:
        if aux.desempilha() != letra:
            return False
    return True