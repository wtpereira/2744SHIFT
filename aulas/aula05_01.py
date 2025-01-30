tabela_categorias = [
    {
        'nome': 'Romance'
    },
    {
        'nome': 'Terror'
    },
    {
        'nome': 'Novela'
    }
]

for index, categoria in enumerate(tabela_categorias):
    print(index, categoria)

try:
    categoria_id = input('Digite o ID da categoria: ')
    categoria_id = int(categoria_id)  # Pode ocorrer em erro
    print('Após int(categoria_id)')
    print(tabela_categorias[categoria_id]) # Pode ocorrer em erro
    print('Após o tabela_categorias[categoria_id]')
    # print(1 / 0)  # Vai ocorrer em erro
except IndexError:
    print(f'ID "{categoria_id}" não encontrado na tabela.')
except ValueError:
    print(f'ID deve ser somente número inteiro. "{categoria_id}" não é um ID válido.')
except Exception as ex:  # Trata todos os tipos de exceção não tratados nas linhas acima.
    print(f'Ocorreu um erro: "{ex}" do tipo "{type(ex)}"')
else:  # then
    print('Não occoreu nenhum erro/exceção.')
finally:
    print('Será executado de qualquer forma.')

"""
tamanho = len(tabela_categorias)
if categoria_id >=0 and categoria_id < tamanho:
    print(tabela_categorias[categoria_id])
else:
    print('ID não encontrado na tabela')
"""

print('Fim!')
