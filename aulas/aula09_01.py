class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):  # Formato que você deseja que o usuário visualize o seu objeto
        return f'Nome: {self.nome}'

    def __repr__(self):  # Formato que você deseja visuaizar o objeto.
        return f'{self.__class__.__name__}("{self.nome}")'


print(f'__name__ do módulo aula09_01: {__name__}')


if __name__ == '__main__':
    d = {
        'nome' : 'João'
    }

    print(d)

    a = Aluno('Well')
    print(a)
