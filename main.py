from service.autor_service import AutorService
from service.categoria_service import CategoriaService
from service.editora_service import EditoraService
from service.livro_service import LivroService

menu_principal = """[Menu Principal] Escolha uma das seguintes opções:
1 - Categorias
2 - Editoras
3 - Autores
4 - Livros
0 - Sair do programa
"""


autor_service = AutorService()
categoria_service = CategoriaService()
editora_service = EditoraService()
livro_service = LivroService()


def display_menu_principal():
    while True:
        print(menu_principal)

        print()  # Uma linha vazia.

        opcao_principal = input('Digite a opção: ')
        match opcao_principal:
            case '0':
                return  # encerra a execução desta função e retorna para onde foi chamada.
            case '1':
                categoria_service.menu()
            case '2':
                editora_service.menu()
            case '3':
                autor_service.menu()
            case '4':
                livro_service.menu()
            case _:
                print('Opção Inválida!')


if __name__ == '__main__':
    display_menu_principal()
    print('Programa Encerrado!')