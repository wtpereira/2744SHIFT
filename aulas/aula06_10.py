# Tipagens ou anotações de tipo


def funcao(a: int, b: int) -> int:
    """Calcula  a elevado a b

    Args:
        a (int): base
        b (int): expoente

    Returns:
        int: Resultado da exponenciação.
    """
    return a ** b


print(f'Resultado: {funcao(2, 5)}')

print('Fim do programa!')
