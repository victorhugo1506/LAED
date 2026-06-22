pilha = []


def empilha(val):
    pilha.append(val)


def desempilha():
    return pilha.pop()


def avaliar_posfixa(expr):
    for c in expr:
        if c.isdigit():
            empilha(int(c))
        else:
            if len(pilha) < 2:
                print("Erro na expressão!")
                return
            val2 = desempilha()
            val1 = desempilha()
            if c == '+':
                empilha(val1 + val2)
            elif c == '-':
                empilha(val1 - val2)
            elif c == '*':
                empilha(val1 * val2)
            elif c == '/':
                empilha(val1 // val2)

    print(f"Resultado da avaliação pós-fixa: {desempilha()}")


expr = "53+2*"
avaliar_posfixa(expr)