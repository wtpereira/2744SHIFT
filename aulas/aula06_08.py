def saudacao(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave} - {valor}')


saudacao(nome='Well', idade=15)
