# Escreva uma função que aceite uma string como parâmetro e retorne o seu inverso (de trás para frente)

def inverte_string(msg: str) -> str:
    return msg[::-1]

mensagem = 'abcdefg-'
# resultado = []

# tamanho = len(mensagem)

# for index in range(tamanho, 0, -1):
#     letra = mensagem[index - 1]
#     print(letra)
#     resultado.append(letra)
#     tamanho -= 1

# print(resultado)
# print(''.join(resultado))

print(inverte_string(mensagem))
