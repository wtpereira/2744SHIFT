falsy = [False, 0, '', 0.0, [], tuple(), {}, set()]
truthy = [True, 10, 'fiap', 3.14, (1, 2, 4), {'chave': 'valor'}, {6, 7, 8} ]

for element in falsy:
    if element:
        print('verdadeiro!')
    else:
        print('False!')

for element in truthy:
    if element:
        print('verdadeiro!')
    else:
        print('False!')


lista = [1, 2, 3]

if lista:
    print('Lista cheia.')
else:
    print('Lista vazia')
