def saudacao():
    while True:
        print('Olá Mundo!')
        opcao = input('Deseja continuar? ')
        if opcao != 's':
            return

    print('Fim da saudacao().')  ## Nunca será executado com o 'return' acima.


resultado = saudacao()
print(resultado)

print('Fim do programa!')
