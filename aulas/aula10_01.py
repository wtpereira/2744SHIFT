# def soma(a, b):
#     return a + b

soma = lambda a, b: a + b

print(soma(34, 56))


# def media(*args):
#     return sum(args)/len(args)

media = lambda *args: sum(args)/len(args)

print(media(40, 50, 60))
print(media(1, 2, 3, 4, 5, 6, 7, 8))
