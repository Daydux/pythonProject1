ten = []
for i in range(1, 11):
    ten.append(i)

print(ten)

evens = list(filter(lambda x: x % 2 == 0, ten))

print(evens)

evens_square = list(map(lambda x: x ** 2, evens))

print(evens_square)

print('Возможными для ввода индексы являются от 0 до 9 или же от -10 до 0. ',
      'Для выхода из функции напечатайте 1111.', sep='\n')


def def_func(teni=None):
    if teni is None:
        teni = ten
    while True:
        try:
            index_user = int(input('Введите индекс: '))
            if index_user == 1111:
                print('exit...')
                break
            print(teni[index_user])
        except IndexError:
            print('Вы вышли за грани возможно вписуемых индексов. Возможными являются от 0 до 9 или же от -10 до 0.')


print(def_func())
