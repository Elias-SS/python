nome = input('Digite o nome do aluno \n') ## não há necessidade de marcar str
n1 = float(input('Digite a 1ª nota de 0 a 100 \n')) ## Está faltando o limites das notas (0 a 100)
n2 = float(input('Digite a 2ª nota de 0 a 100\n'))
n3 = float(input('Digite a 3ª nota de 0 a 100\n'))
n4 = float(input('Digite a 4ª nota de 0 a 100\n'))
media = int((2*(n1+n2)+3*(n3+n4))/10)
if media >=60:
    print(f'\033[30:42m O aluno {nome} obteve a media {media} e está aprovado\033[m')
elif media < 20:
    print (f'\033[41m O aluno {nome} obteve a media {media} e está reprovado\033[m')
elif 20 <= media <= 59:
    print (f'\033[0;43;31m O aluno {nome} obteve a media {media} e está em recuperação\033[m')

