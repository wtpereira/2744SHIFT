print('Início do programa.')

def valida_email(email: str) -> bool:
    email = email.lower()
    if email.find('@') >=0 and email.endswith('.com'):
        return True

    return False


class Autor:
    __slots__ = ['__nome', '__email', '__fone', '__biografia']
    def __init__(self, nome: str, fone: str=None, biografia: str=None):  # construtor
        self.nome = nome
        self.__email = None
        self.fone = fone
        self.biografia = biografia

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


autor = Autor("machado de assis", '11', 'bioxxxxx')

try:
    autor.email = "x@teste.com"
except Exception as ex:
    print(ex)

print(autor)
print(autor.nome)
print(autor.email)
print(autor.biografia)

outro_autor = Autor('CECILIA MEIRELES')
try:
    outro_autor.email = 'x@y'
except Exception as ex:
    print(ex)

outro_autor.nome = 'CECILIA MEIRELES silva'
outro_autor.fone ='22222'
outro_autor.biografia = 'bio da cecília'

print(outro_autor.email)
print('Fim do programa.')
