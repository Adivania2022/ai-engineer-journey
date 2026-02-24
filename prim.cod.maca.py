from random import randint


caixa_de_maças = 100
balde = 0
while balde <= caixa_de_maças:
    menino_joga = randint(1, 4)
    print(f"O menino jogou {menino_joga} maças.")
    balde += menino_joga
    print(f"Existem no balde {balde} maças.")
print(f"A caixa de maças encheu com mais de {caixa_de_maças} maças pois no balde foram jogadas {balde} maças peo menino. ")