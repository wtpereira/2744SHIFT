print('Início do programa.')

# dict_autor = {
#     'nome': 'Cecília',
#     'email': 'cecilia.com'
# }

# print(dict_autor)
# print(dict_autor['nome'])
# print(dict_autor['email'])

def valida_email(email: str) -> bool:
    email = email.lower()
    if email.find('@') >=0 and email.endswith('.com'):
        return True

    return False


class Autor:
    def __init__(self):  # construtor
        print('Estou no construtor.')
        self.nome = None
        self.email = None
        self.fone = None
        self.biografia = None

    def get_email(self):  # getter
        return self.email

    def set_email(self, em):  # setter
        if valida_email(em):
            self.email = em
            return
        ex = Exception('E-mail inválido')
        ex.meu_codigo = 'EX000100'
        raise ex



autor = Autor()


autor.nome = "Machado"
try:
    autor.set_email("x@teste.com")
except Exception as ex:
    print(ex)

print(autor)
print(autor.nome)
print(autor.get_email())
print(autor.biografia)


outro_autor = Autor()
outro_autor.nome = 'Cecília'
try:
    outro_autor.set_email('x@y')
except Exception as ex:
    outro_autor.email = 'x@y'
    print(ex, ex.meu_codigo)

print('Fim do programa.')
