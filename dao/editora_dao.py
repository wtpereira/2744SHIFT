from model.editora import Editora

class EditoraDAO:
    __slots__ = ['__tabela_editoras']
    def __init__(self):
        self.__tabela_editoras = []

    def empty(self) -> bool:
        return len(self.__tabela_editoras) == 0

    def listar(self) -> list[Editora]:
        return self.__tabela_editoras

    def adicionar(self, editora: Editora) -> None:
        self.__tabela_editoras.append(editora)

    def remover(self, editora_id: int) -> bool:
        encontrado = False

        for index, editora in enumerate(self.__tabela_editoras):
            if editora.id == editora_id:
                encontrado = True
                break

        if encontrado:
            self.__tabela_editoras.pop(index)

        return encontrado

    def buscar_por_id(self, editora_id) -> Editora:
        for editora in self.__tabela_editoras:
            if (editora.id == editora_id):
                return editora
