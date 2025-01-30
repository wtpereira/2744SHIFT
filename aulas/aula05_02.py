try:
    print(1 / 0)
except Exception as ex:
    try:
        print(2 / 0)
    except:
        print('Resolvido!')
finally:
    print('Finally!')
