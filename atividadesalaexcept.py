def tela_de_inicio():
    print("Menu:\n")
    print("Go - Para iniciar algoritmo de divisão")
    print("Exit - Para Sair")
    
    comando = input("Digite o comando: ")
    
    match comando.lower():
        case "go":
            algoritmo()
        case "exit":
            exit()
        case _:
            print("Comando inválido")
            tela_de_inicio()

def algoritmo():
    while True:
        try:
            print("Algoritmo de Divisão \n\n")

            n1 = int(input("Digite o dividendo: \n"))
            n2 = int(input("Digite o divisor(Nao pode ser 0): \n"))
            resultado = float(n1 / n2)
            print(f"O resultado da divisão é {resultado:.3f}")
            tela_de_inicio()

        except ValueError:
            print("Erro: Digite um numero inteiro")
        except ZeroDivisionError:
            print("Erro: Não é possivel dividir por 0")


tela_de_inicio()