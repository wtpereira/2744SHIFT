import itertools
from model.utils import valida_email


class Autor:
    id_autor = itertools.count(start=1)  # atributo de classe
    __slots__ = ['__id', '__nome', '__email', '__fone', '__biografia']

    def __init__(self, nome: str, fone: str=None, biografia: str=None):  # construtor
        self.id = next(Autor.id_autor)
        self.nome = nome
        self.__email = None
        self.fone = fone
        self.biografia = biografia

    def __str__(self):
        return f'{self.id} | {self.nome} | {self.email} | {self.fone} | {self.biografia}'

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.nome}", "{self.fone}", "{self.biografia}")'

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome.title()

    @property
    def email(self):  # getter
        return self.__email

    @email.setter
    def email(self, em: str):  # setter
        if valida_email(em):
            self.__email = em.lower()
            return
        ex = Exception('E-mail inválido!')
        raise ex

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, fone):
        self.__fone = fone

    @property
    def biografia(self):
        return self.__biografia

    @biografia.setter
    def biografia(self, biografia):
        self.__biografia = biografia
