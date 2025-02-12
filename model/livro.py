import itertools

from model.autor import Autor
from model.categoria import Categoria
from model.editora import Editora


class Livro:
    __slots__ = ['__id', '__titulo', '__resumo', '__ano', '__paginas', '__isbn', '__autor', '__categoria', '__editora']
    id_livro = itertools.count(start=1)  # atributo de classe

    def __init__(self, titulo: str, resumo: str, ano: str, paginas: str, isbn: str):
        self.id = next(Livro.id_livro)
        self.titulo = titulo
        self.resumo = resumo
        self.ano = ano
        self.paginas = paginas
        self.isbn = isbn

    def __str__(self):
        return f"{self.id} | {self.titulo} | {self.ano} | {self.paginas} | {self.isbn} | {self.autor.nome} | {self.categoria.nome} | {self.editora.nome}"

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo.title()

    @property
    def resumo(self) -> str:
        return self.__titulo

    @resumo.setter
    def resumo(self, resumo: str):
        self.__resumo = resumo

    @property
    def ano(self) -> str:
        return self.__ano

    @ano.setter
    def ano(self, ano: str):
        self.__ano = ano

    @property
    def paginas(self) -> str:
        return self.__paginas

    @paginas.setter
    def paginas(self, paginas: str):
        self.__paginas = paginas

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def autor(self) -> Autor:
        return self.__autor

    @autor.setter
    def autor(self, autor: Autor):
        self.__autor = autor

    @property
    def categoria(self) -> Categoria:
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria: Categoria):
        self.__categoria = categoria

    @property
    def editora(self) -> Editora:
        return self.__editora

    @editora.setter
    def editora(self, editora: Editora):
        self.__editora = editora
