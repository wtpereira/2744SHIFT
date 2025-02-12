import itertools


class Categoria:
    __slots__ = ['__id', '__nome']
    id_categoria = itertools.count(start=1)

    def __init__(self, nome: str) -> None:
        self.__id: int = next(Categoria.id_categoria)
        self.__nome: str = nome

    def __str__(self) -> str:
        return f'{self.id} | {self.nome}'

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome
