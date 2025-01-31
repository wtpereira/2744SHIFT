def func(*args, **kwargs):
    for elemento in args:
        print(elemento)
    print('-' * 40)
    for chave, valor in kwargs.items():
        print(f'{chave} = {valor}')
    print('-' * 40)


func(10, True, 12.345, nome='Well', sobrenome='Pereira', idade=20)

print('Fim do programa!')
