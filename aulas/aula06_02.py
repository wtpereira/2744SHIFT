def saudacao(nome_usuario='usuário'):
    print(f'Olá, {nome_usuario}!')


nome = input('Digite o seu nome: ')
if nome == '':
    saudacao()
else:
    saudacao(nome)


#
#
#

outro_nome = input('Digite o seu nome: ')

if outro_nome == '':
    saudacao()
else:
    saudacao(outro_nome)

print('Fim do programa!')

