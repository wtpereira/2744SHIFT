def fatorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    return n * fatorial(n - 1)

a = int(input('Digite um valor inteiro: '))
resp = fatorial(a)
print(f'O fatorial de {a} é {resp}')
