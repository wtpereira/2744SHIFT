from model.livro import Livro
class LivroDAO:
    _slots__ = ['__tabela_livros']

    def __init__(self):
        self.__tabela_livros = []

    def empty(self) -> bool:
        return len(self.__tabela_livros) == 0

    def listar(self) -> list[Livro]:
        return self.__tabela_livros

    def adicionar(self, novo_livro: Livro):
        self.__tabela_livros.append(novo_livro)

    def remover(self, livro_id: int) -> bool:
        encontrado = False
        for index, livro in enumerate(self.__tabela_livros):
            if livro.id == livro_id:
                encontrado = True
                break

        if encontrado:
            self.__tabela_livros.pop(index)

        return encontrado

    def buscar_por_id(self, livro_id: int):
        for livro in self.__tabela_livros:
            if livro.id == livro_id:
                return livro

