from random import randint
sorteio = []
cont = 0
print("<" * 5, " SORTEIO MEGA-SENA ", ">" * 5)
while True:
    num = randint(1, 51)
    if num not in sorteio:
        sorteio.append(num)
        cont += 1
    if cont >= 6:
        break
print("Os números sorteados foram {}".format(sorted(sorteio)))