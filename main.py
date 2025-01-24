menu_principal = """[Menu Principal] Escolha uma das seguintes opções:
1 - Categorias
2 - Editoras
3 - Autores
4 - Livros
0 - Sair do programa
"""

menu_autores = """
[Autores] Escolha uma das seguintes opções:
1 - Listar todas os autores
2 - Adicionar novo autor
3 - Excluir autor
4 - Ver autor por Id
0 - Voltar ao menu anterior
"""

tabela_autores = []

while True:
    print(menu_principal)

    print()  # Uma linha vazia.

    opcao_principal = input('Digite a opção: ')

    if opcao_principal == '3':
        while True:
            print(menu_autores)
            opcao_autores = input('Digite a opção: ')
            if opcao_autores == '0':
                break  # interrompe o loop do while autores
            if opcao_autores == '1':
                if tabela_autores == []:
                    print("Nenhum Autor cadastrado.")
                else:
                    print('Id | Nome | Email | Telefone | Biografia')
                    for index, autor in enumerate(tabela_autores):
                        print(f'{index} | {autor[0]} | {autor[1]} | {autor[2]} | {autor[3]}')
            if opcao_autores == '2':
                nome_autor = input('Digite o nome do autor: ')
                email_autor = input('Digite o email do autor: ')
                fone_autor = input('Digite o telefone do autor: ')
                bio_autor = input('Digite a biografia do autor: ')
                novo_autor = []
                novo_autor.append(nome_autor)
                novo_autor.append(email_autor)
                novo_autor.append(fone_autor)
                novo_autor.append(bio_autor)
                tabela_autores.append(novo_autor)
                print('Autor adicionado com sucesso!')
            if opcao_autores == '3':
                id = int(input('Digite o ID do autor a ser excluido: '))
                tabela_autores.pop(id)
                print('Autor excluído com sucesso!')
            if opcao_autores == '4':
                id = int(input('Digite o ID do autor para buscar: '))
                autor = tabela_autores[id]
                print('Id | Nome | Email | Telefone | Biografia')
                print(f'{id} | {autor[0]} | {autor[1]} | {autor[2]} | {autor[3]}')
    if opcao_principal == '0':
        break  # interrompe o loop do while principal

print('Programa Encerrado!')
