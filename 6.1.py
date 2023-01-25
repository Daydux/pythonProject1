# def - definition (определение)

# def greet(name, surname): #name - обязательный позиционный параметр
#     print(f"name: {name}, surname: {surname}") #keyboard arguments (именованые аргументы)
#
#
# greet('Chel', 'Chort')
# greet('Chert', 'Gnidch')
# greet('Chertilla', 'Apchoo')

# def len1(seq):
#     counter = 0
#     for i in seq:
#         counter += 1
#     return counter
#
# print(len1(input('word: ')))
# print(len('python'))


# def plus(a, b=2, *args):
#     print(a, b, args)
#     return sum(args) / a * b
#
# print(plus(17,35, 23, 71, 54))

# def menu(**kwargs):
#     # return sum(kwargs.values())
#     return kwargs
# print(menu(a=1, b=2, c=7))

students_rate = {
    'bogdan': 4,
    'marsel': 3,
    'alan': 5
}


def find_student(name):
    if name in students_rate.keys():
        return True
    return False


def add(name: str, rate: int):
    if name not in students_rate.keys():
        if rate in range(1, 6):
            students_rate[name] = rate
        else:
            print('только от нуля до пяти')
    else:
        print(f'{name} такое имя есть!')


def delete(name):
    if name in students_rate.keys():
        del students_rate[name]
    else:
        print(f'{name} такого имени нет!')


def edit(name, new_name):
    if name in students_rate.keys():
        students_rate[new_name] = students_rate.pop(name)


while True:
    print(students_rate)
    command = input(f'1) add\n'
                    f'2) edit\n'
                    f'3) delete\n')
    if command == '1':
        add(name=input('новое имя: '), rate=int(input('оценка:')))
    elif command == '2':
        edit(name=input('старое имя: '), new_name=input('новое имя: '))
    elif command == '3':
        delete(name=input('старое имя: '))
    else:
        print('Такого выбора нет.')

print(students_rate)

# def get_square(width: int, length: int) -> int:
#     """
#     Принимает 2 значения ширина, длина.
#     Возвращает площадь (целое число)
#     """
#     return width * length
#
# square_2 = get_square(5, 7)
# square_hall = get_square(7, 15)
# print(square_2, square_hall, sep='\n')
# print(get_square.__doc__)
# print(help(get_square))


# width = 7
# length = 15
# square_hall = width * length
# print(square_hall)

# Don't repeat yourself
