numero = int(input('Digite um número inteiro positivo para obter a tabuada: '))

while numero <= 0:  # enquanto numero menor que zero execute o bloco abaixo:
    print('Não pode número negativo.')
    numero = int(input('Digite um número inteiro positivo para obter a tabuada: '))

i = 1  # inicializando a variável 'i' com o valor 1

while i < 11:
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
    i += 1  # i = i + 1

# enquanto a condição estiver sendo satisfeita, execute o bloco.