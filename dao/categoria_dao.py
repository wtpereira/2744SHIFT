from model.categoria import Categoria

class CategoriaDAO:
    __slots__ = ['__tabela_categorias']

    def __init__(self):
        self.__tabela_categorias = []

    def empty(self) -> bool:
        return len(self.__tabela_categorias) == 0

    def listar(self) -> list[Categoria]:  # SELECT * FROM categoria
        return self.__tabela_categorias

    def adicionar(self, categoria: Categoria) -> None:  # INSERT INTO categoria
        self.__tabela_categorias.append(categoria)

    def remover(self, categoria_id: int) -> bool:
        encontrado = False

        for index, categoria in enumerate(self.__tabela_categorias):
            if categoria.id == categoria_id:
                encontrado = True
                break

        if encontrado:
            self.__tabela_categorias.pop(index)

        return encontrado

    def buscar_por_id(self, categoria_id) -> Categoria:
        for categoria in self.__tabela_categorias:
            if categoria.id == categoria_id:
                return categoria
