ed = [[0], [1,2,3], [4,5,6], [7,8,9], [10]]
relatorio = []

def classificar(niveldedor):
    if niveldedor == 0:
        return "Sem dor"
    elif niveldedor in [1, 2, 3]:
        return "Nível de dor fraco"
    elif niveldedor in [4, 5, 6]:
        return "Nível de dor moderado"
    elif niveldedor in [7, 8, 9]:
        return "Nível de dor intenso"
    elif niveldedor == 10:
        return "Nível de dor insuportável"
    else:
        return "Nível inválido"

def encontrar_posicao(niveldedor):
    for i in range(len(ed)):
        for j in range(len(ed[i])):
            if ed[i][j] == niveldedor:
                return f"linha {i}, coluna {j}"

def registrar(niveldedor):
    classificacao = classificar(niveldedor)
    posicao = encontrar_posicao(niveldedor)
    entrada = f"Nível de dor: {niveldedor} | {classificacao} | Posição na matriz: {posicao}"
    relatorio.append(entrada)
    print(entrada)

niveldedor = int(input("Digite o número do nível de dor: "))
melhorou = int(input("O paciente melhorou? (Digite 1 para sim e 0 para não): "))
registrar(niveldedor)

while melhorou != 1:
    niveldedor = int(input("Digite o número do nível de dor: "))
    melhorou = int(input("O paciente melhorou? (Digite 1 para sim e 0 para não): "))
    registrar(niveldedor)

relatorio.append("Paciente melhorou.")

print("\nRelatório final:")
for item in relatorio:
    print(item)