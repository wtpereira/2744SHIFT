from model.autor import Autor

class AutorDAO:
    __slots__ = ['__tabela_autores']

    def __init__(self):
        self.__tabela_autores = []

    def empty(self) -> bool:
        return len(self.__tabela_autores) == 0

    def listar(self) -> list[Autor]:
        # Nesse método, conecto ao banco de dados e busco todos os registros de Autores
        return self.__tabela_autores

    def adicionar(self, novo_autor: Autor):
        self.__tabela_autores.append(novo_autor)
    def remover(self, autor_id: int) -> bool:
        encontrado = False
        for index, autor in enumerate(self.__tabela_autores):
            if autor.id == autor_id:
                encontrado = True
                break

        if encontrado:
            self.__tabela_autores.pop(index)

        return encontrado

    def buscar_por_id(self, autor_id: int):
        for autor in self.__tabela_autores:
            if autor.id == autor_id:
                return autor

    def editar(self, autor_id: int):
        for autor in self.__tabela_autores:
            if autor.id == autor_id:
                return autor
