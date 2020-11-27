from random import randint
from time import sleep
computador = randint(0,5)# Faz o computudador pensar
print('-=-' * 20)
print('Vou pensar no numero entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #jogador tente advinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns!Você conseguiu me vencer!')
else:
    print('Ganhei! EU pensei no número {} e não no número {}!'.format(computador, jogador))