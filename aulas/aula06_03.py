def soma(*args):
    resp = 0
    for elemento in args:
        resp += elemento

    return resp


resultado = soma(10, 20, 30, 40, 50)
print(f'O resultado da soma é {resultado}')

outro_resultado = soma()
print(f'O resultado da soma é {outro_resultado}')
