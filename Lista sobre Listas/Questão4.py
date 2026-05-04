import random 

l = ["Victor", "Vinicius", "Arthur", "Gabriela", "João Bosco"]
n = 0

for i in range(len(l)):
    n = random.randint(0, len(l) - 1)
    print(l.pop(n))