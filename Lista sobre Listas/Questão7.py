v = [1, 1, 1, 2, 3, 5, 8, 13, 13, 13]
contador = 0
numerostrinca = []

for i in range(2, 10):
    if v[i] == v[i-1] == v[i-2]:
        contador += 1
    if contador == 1:
        numerostrinca.append(v[i])
    contador = 0

print("Números que aparecem exatamente 3 vezes:", numerostrinca)