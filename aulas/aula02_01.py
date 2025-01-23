a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))

media = (a + b) / 2

if media < 5:
    print(f'Reprovado com a média: {media}')
else:
    print(f'Aprovado com a média: {media}')

if media == 10:
    print('Arrasou!')
    print(f'Por causa da média {media} você ganhou uma bolsa de estudos!')
