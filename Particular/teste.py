from random import randint

l: list = []
for i in range(4):
    j = {"jogos": randint(0, 6)}
    l.append(j.copy())
    j.clear()
print(l[1]["jogos"])
