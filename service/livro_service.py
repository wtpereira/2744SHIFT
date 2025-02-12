from dao.livro_dao import LivroDAO
from dao.autor_dao import AutorDAO
from dao.categoria_dao import CategoriaDAO
from dao.editora_dao import EditoraDAO

from service.autor_service import AutorService
from service.categoria_service import CategoriaService
from service.editora_service import EditoraService

from model.livro import Livro

menu_livros = """
[Livros] Escolha uma das seguintes opções:
1 - Listar todos os livros
2 - Adicionar novo livro
3 - Excluir livro
4 - Ver livro por Id
0 - Voltar ao menu anterior
"""


class LivroService:
    livro_dao = LivroDAO()

    def menu(self):
        print(menu_livros)
        opcao_autores = input('Digite a opção: ')
        match opcao_autores:
            case '0':
                return  # encerra a execução desta função e retorna para onde foi chamada.
            case '1':
                self.listar()
            case '2':
                self.adicionar()
            case '3':
                self.remover()
            case '4':
                self.mostrar_por_id()
            case '5':
                self.editar()
            case _:
                print('Opção Inválida! Por favor, tente novamente')

        self.menu()

    def listar(self):
        livros = LivroService.livro_dao.listar()
        if livros:
            print('Id | Título | Ano | Qtde páginas | ISBN | autor | categoria | editora')
            for livro in livros:
                print(livro)
        else:
            print('Nenhum livro cadastrado.')
            input('Pressione <ENTER> para continuar.')

    def adicionar(self):
        if AutorService.autor_dao.empty()  or CategoriaService.categoria_dao.empty() or EditoraService.editora_dao.empty():
            print('Necessário cadastrar pelo menos um autor, uma categoria, e uma editora.')
            return

        titulo = input('Digite o título do livro: ')
        resumo = input('Digite o resumo do livro: ')
        ano = input('Digite o ano de publicação: ')
        paginas = input('Digite a quantidade de páginas: ')
        isbn = input('Digite o ISBN: ')

        print('Id | Nome | Email')
        for autor in AutorService.autor_dao.listar():
            print(f'{autor.id} | {autor.nome} | {autor.email}')

        autor_id = int(input('Digite o Id do autor: '))

        print('Id | Nome')
        for categoria in CategoriaService.categoria_dao.listar():
            print(categoria)

        categoria_id = int(input('Digite o Id da categoria: '))

        print('Id | Nome')
        for editora in EditoraService.editora_dao.listar():
            print(f"{editora.id} | {editora.nome}")

        editora_id = int(input('Digite o Id da editora: '))

        novo_livro = Livro(titulo, resumo, ano, paginas, isbn)
        novo_livro.autor = AutorService.autor_dao.buscar_por_id(autor_id)
        novo_livro.categoria = CategoriaService.categoria_dao.buscar_por_id(categoria_id)
        novo_livro.editora = EditoraService.editora_dao.buscar_por_id(editora_id)

        try:
            LivroService.livro_dao.adicionar(novo_livro)
        except Exception as ex:
            print(f'Erro ao tentar inserir novo livro: {ex}')
        else:
            print('Livro adicionado com sucesso!')
    def remover(self):
        if LivroService.livro_dao.empty():
            print('Nenhum livro cadastrado.')
            input('Pressione <ENTER> para continuar.')
            return

        try:
            id = int(input('Digite o ID do livro a ser excluido: '))
            if LivroService.livro_dao.remover(id):
                print('Livro excluído com sucesso!')
            else:
                print(f'Id do livro "{id}" inválido.')
        except Exception as ex:
            print(f'Erro ao tentar excluir livro: {ex}')

    def mostrar_por_id(self):
        if LivroService.livro_dao.empty():
            print('Nenhum livro cadastrado.')
            input('Pressione <ENTER> para continuar.')
            return

        try:
            id = int(input('Digite o ID do livro a ser excluido: '))
            livro = LivroService.livro_dao.buscar_por_id(id)
            if livro:
                print('Id | Título | Ano | Qtde páginas | ISBN | autor | categoria | editora')
                print(livro)
            else:
                print(f'Id do livro "{id}" inválido.')
        except Exception as ex:
            print(f'Erro ao buscar livro por ID: {ex}')
