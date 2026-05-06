import random
from collections import Counter

naipes = ['♠', '♥', '♦', '♣']
valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

baralho = [f"{valor}{naipe}" for valor in valores for naipe in naipes]
random.shuffle(baralho)

mao = [baralho.pop() for _ in range(5)]

def extrair(carta):
    return carta[:-1], carta[-1]

def valor_numerico(v):
    ordem = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}
    return ordem[v]

def identificar_mao(mao):
    vals = [extrair(c)[0] for c in mao]
    naipes_mao = [extrair(c)[1] for c in mao]
    nums = sorted([valor_numerico(v) for v in vals])

    flush = len(set(naipes_mao)) == 1
    sequencia = (nums == list(range(nums[0], nums[0] + 5)))

    if nums == [2, 3, 4, 5, 14]:
        sequencia = True
        nums = [1, 2, 3, 4, 5]

    contagem = Counter(vals)
    grupos = sorted(contagem.values(), reverse=True)

    if flush and sequencia:
        if nums[-1] == 14:
            return "Royal Flush"
        return "Straight Flush"
    if grupos == [4, 1]:
        return "Quadra (Four of a Kind)"
    if grupos == [3, 2]:
        return "Full House"
    if flush:
        return "Flush"
    if sequencia:
        return "Sequência (Straight)"
    if grupos == [3, 1, 1]:
        return "Trinca (Three of a Kind)"
    if grupos == [2, 2, 1]:
        return "Dois Pares"
    if grupos == [2, 1, 1, 1]:
        return "Um Par"
    return "Carta Alta (High Card)"

print("Sua mão:")
for i, carta in enumerate(mao, 1):
    print(f"  Carta {i}: {carta}")

print(f"\nResultado: {identificar_mao(mao)}")