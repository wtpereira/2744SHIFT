menu_principal = """[Menu Principal] Escolha uma das seguintes opções:
1 - Categorias
2 - Editoras
3 - Autores
4 - Livros
0 - Sair do programa
"""

menu_autores = """
[Autores] Escolha uma das seguintes opções:
1 - Listar todos os autores
2 - Adicionar novo autor
3 - Excluir autor
4 - Ver autor por Id
0 - Voltar ao menu anterior
"""

menu_categorias = """
[Categorias] Escolha uma das seguintes opções:
1 - Listar toda as categorias
2 - Adicionar nova categoria
3 - Excluir categoria
4 - Ver categoria por Id
0 - Voltar ao menu anterior
"""

menu_editoras = """
[Editoras] Escolha uma das seguintes opções:
1 - Listar todas as editoras
2 - Adicionar nova editora
3 - Excluir editora
4 - Ver editora por Id
0 - Voltar ao menu anterior
"""

tabela_autores = []
tabela_categorias = []
tabela_editoras = []

while True:
    print(menu_principal)

    print()  # Uma linha vazia.

    opcao_principal = input('Digite a opção: ')
    match opcao_principal:
        case '0':
            break  # interrompe o loop do while principal
        case '1':
            while True:
                print(menu_categorias)
                opcao_categorias = input('Digite a opção: ')
                match opcao_categorias:
                    case '0':
                        break  # interrompe o loop do while categorias
                    case '1':
                        if tabela_categorias == []:
                            print("Nenhuma Categoria cadastrada.")
                            input("Pressione <ENTER> para continuar.")
                            continue

                        print('Id | Nome')
                        for index, categoria in enumerate(tabela_categorias):
                            print(f"{index} | {categoria['nome']}")
                    case '2':
                        nome_categoria = input('Digite o nome da categoria: ')
                        nova_categoria = {
                            'nome': nome_categoria
                        }
                        tabela_categorias.append(nova_categoria)
                    case '3':
                        if tabela_categorias == []:
                            print("Nenhuma Categoria cadastrada.")
                            input("Pressione <ENTER> para continuar.")
                            continue

                        id = int(input('Digite o ID da categoria a ser excluída: '))
                        tabela_categorias.pop(id)
                        print('Categoria excluída com sucesso!')
                    case '4':
                        if tabela_categorias == []:
                            print("Nenhuma Categoria cadastrada.")
                            input("Pressione <ENTER> para continuar.")
                            continue

                        id = int(input('Digite o ID da categoria para buscar: '))
                        categoria = tabela_categorias[id]
                        print('Id | Nome')
                        print(f"{id} | {categoria['nome']}")
                    case _:
                        print('Opção inválida!')
        case '2':
            while True:
                print(menu_editoras)
                opcao_editoras = input('Digite a opção: ')
                match opcao_editoras:
                    case '0':
                        break  # interrompe o loop do while editoras
                    case '1':
                        if tabela_editoras == []:
                            print("Nenhuma Editora cadastrada.")
                            input("Pressione <ENTER> para continuar.")
                            continue

                        print('Id | Nome | Endereço | Telefone')
                        for index, editora in enumerate(tabela_editoras):
                            print(f"{index} | {editora['nome']} | {editora['endereco']} | {editora['fone']}")
                    case '2':
                        nome_editora = input('Digite o nome da editora: ')
                        endereco_editora = input('Digite o endereço da editora: ')
                        fone_editora = input('Digite o telefone da editora: ')
                        nova_editora = {}
                        nova_editora['nome'] = nome_editora
                        nova_editora['endereco'] = endereco_editora
                        nova_editora['fone'] = fone_editora
                        tabela_editoras.append(nova_editora)
                        print('Editora adicionada com sucesso!')
                    case '3':
                        if tabela_editoras == []:
                            print("Nenhuma Editora cadastrada.")
                            input("Pressione <ENTER> para continuar.")
                            continue

                        id = int(input('Digite o ID da editora a ser excluída: '))
                        tabela_editoras.pop(id)
                        print('Editora excluída com sucesso!')
                    case '4':
                        if tabela_editoras == []:
                            print("Nenhuma Editora cadastrada.")
                            input("Pressione <ENTER> para continuar.")
                            continue

                        id = int(input('Digite o ID da editora para buscar: '))
                        editora = tabela_editoras[id]
                        print('Id | Nome | Endereço | Telefone')
                        print(f"{id} | {editora['nome']} | {editora['endereco']} | {editora['fone']}")
                    case _:  # opção default
                        print('Opção inválida!')
        case '3':
            while True:
                print(menu_autores)
                opcao_autores = input('Digite a opção: ')
                match opcao_autores:
                    case '0':
                        break  # interrompe o loop do while autores
                    case '1':
                        if tabela_autores == []:
                            print("Nenhum Autor cadastrado.")
                            input("Pressione <ENTER> para continuar.")
                            continue

                        print('Id | Nome | Email | Telefone | Biografia')
                        for index, autor in enumerate(tabela_autores):
                            print(f'{index} | {autor['nome']} | {autor['email']} | {autor['fone']} | {autor['biografia']}')
                    case '2':
                        nome_autor = input('Digite o nome do autor: ')
                        email_autor = input('Digite o email do autor: ')
                        fone_autor = input('Digite o telefone do autor: ')
                        bio_autor = input('Digite a biografia do autor: ')
                        novo_autor = {
                            'nome': nome_autor,
                            'email': email_autor,
                            'fone': fone_autor,
                            'biografia': bio_autor
                        }
                        tabela_autores.append(novo_autor)
                        print('Autor adicionado com sucesso!')
                    case '3':
                        if tabela_autores == []:
                            print("Nenhum Autor cadastrado.")
                            input("Pressione <ENTER> para continuar.")
                            continue

                        id = int(input('Digite o ID do autor a ser excluido: '))
                        tabela_autores.pop(id)
                        print('Autor excluído com sucesso!')
                    case '4':
                        if tabela_autores == []:
                            print("Nenhum Autor cadastrado.")
                            input("Pressione <ENTER> para continuar.")
                            continue

                        id = int(input('Digite o ID do autor para buscar: '))
                        autor = tabela_autores[id]
                        print('Id | Nome | Email | Telefone | Biografia')
                        print(f'{id} | {autor['nome']} | {autor['email']} | {autor['fone']} | {autor['biografia']}')
                    case _:
                        print('Opção Inválida!')
        case _:
            print('Opção Inválida!')

print('Programa Encerrado!')
