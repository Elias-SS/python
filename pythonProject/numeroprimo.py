numero = int(input())
divisores = 0
while numero < 1:
    numero = int(input())
for i in range(1, numero+1, 1):
    if numero % i == 0:
        divisores += 1
if divisores <= 2:
    print(f'O numero {numero} é primo')
else:
    print(f'O numero {numero} tem {divisores} divisores, portanto não eh primo')




