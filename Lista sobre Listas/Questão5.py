l = [""] * 31
idades = [0] * 31

autenticador = int(input("Ainda ha aniversariantes esse mes? (Digite 1 para sim e 0 para nao): "))

while autenticador != 0:
    nome = input("Digite o nome do aniversariante: ")
    dia = int(input("Digite o dia do aniversario: "))
    idade = int(input("Quantos anos a pessoa faz?: "))
    
    l[dia - 1] = nome
    idades[dia - 1] = idade

    autenticador = int(input("Ainda ha aniversariantes esse mes? (Digite 1 para sim e 0 para nao): "))

print("Aniversariantes do mes:")
for i in range(len(l)):
    if l[i] != "":
        print("%s faz %d anos no dia %d" % (l[i], idades[i], i + 1))