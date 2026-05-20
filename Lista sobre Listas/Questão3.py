l = [] * 50
n = 0

for i in range(50):
    l.insert(n, "id %d" % n)
    n += 1

print(l)