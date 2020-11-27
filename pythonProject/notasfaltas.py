nota = float(input('Digite sua nota: '))
falta = int(input('Digite a quantidade de vezes faltadas: '))
if nota >= 85 and nota <= 100 and falta <= 10:
    print('Seu conceito na disciplina foi A')
elif nota >= 60 and nota <= 84 and falta <= 10:
    print('Seu conceito na disciplina foi B')
elif nota >= 0 and nota <= 59 and falta <= 10:
    print('Seu conceito na disciplina foi C.')
elif nota >= 85 and nota <= 100 and falta >= 10:
    print('Seu conceito na disciplina foi B.')
elif nota >= 60 and nota <= 84 and falta >= 10:
    print('Seu conceito na disciplina foi C')
if nota >= 0 and nota <= 59 and falta >= 10:
    print('Seu conceito na disciplina foi D')
