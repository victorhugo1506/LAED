def verificar_parenteses(expr):
    saldo = 0

    for i, c in enumerate(expr):
        if c == '(':
            saldo += 1
        elif c == ')':
            saldo -= 1

        if saldo < 0:
            print(f"Erro: Parêntese ')' sobrando na posição {i + 1}")
            return

    if saldo > 0:
        print(f"Erro: Faltou fechar {saldo} parêntese(s).")
    else:
        print("A expressão está balanceada com sucesso!")


expr = "4+(3*(5+2()*5"
verificar_parenteses(expr)