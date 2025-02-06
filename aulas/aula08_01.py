print('Início do programa.')

def valida_email(email: str) -> bool:
    email = email.lower()
    if email.find('@') >=0 and email.endswith('.com'):
        return True

    return False


class Autor:
    __slots__ = ['__nome', '__email', '__fone', '__biografia']
    def __init__(self, nome: str, fone: str=None, biografia: str=None):  # construtor
        print('Estou no construtor.')
        self.__nome = nome.title()
        self.__email = None
        self.__fone = fone
        self.__biografia = biografia


    def get_email(self):  # getter
        return self.__email

    def set_email(self, em):  # setter
        if valida_email(em):
            self.__email = em
            return
        ex = Exception('E-mail inválido')
        raise ex

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_fone(self):
        return self.__fone

    def set_fone(self, fone):
        self.__fone = fone

    def get_biografia(self):
        return self.__biografia

    def set_biografia(self, biografia):
        self.__biografia = biografia


autor = Autor("machado de assis", '11', 'bioxxxxx')

try:
    autor.set_email("x@teste.com")
except Exception as ex:
    print(ex)

print(autor)
print(autor.get_nome())
print(autor.get_email())
print(autor.get_biografia())

outro_autor = Autor('CECILIA MEIRELES')
try:
    outro_autor.set_email('x@y')
except Exception as ex:
    print(ex)

outro_autor.set_fone('22222')
outro_autor.set_biografia('bio da cecília')

print(outro_autor.get_email())
print('Fim do programa.')
