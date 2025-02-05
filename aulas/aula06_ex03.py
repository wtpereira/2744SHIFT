""" Escreva uma função para identificar palíndromos
(é uma palavra, frase ou número que permanece igual quando lida de trás para frente)
"""

def is_palindromo(msg: str) -> bool:
    s = list(msg)
    lista = []
    for letra in s:
        if letra.isalnum():
            lista.append(letra.lower())

    temp = ''.join(lista)
    inverso = temp[::-1]
    return temp == inverso


s1 = "Anotaram a data da maratona"
s2 = "ana"
s3 = "Ana"
s4 = "Anotaram a data de maratona"

print(f'{s2} é palíndromo? {is_palindromo(s2)}')

print(f'{s3} é palíndromo? {is_palindromo(s3)}')

print(f'{s1} é palíndromo? {is_palindromo(s1)}')

print(f'{s4} é palíndromo? {is_palindromo(s4)}')

