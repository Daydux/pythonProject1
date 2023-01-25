# tuple_ = ('alma', [1, 4, 3])
# print([i for i in tuple_[::-1]])
# for i in tuple_:
#     print(i)

# list_ = [range(1, 1000000)]

# array = range(0, 1_000_001)
# print(array)

# list2 = list(filter(lambda x: x % 2 == 0, array))
# print(list2)

# contacts = [
#     {'name': 'Geektech', 'phone': '0507052018'},
#     {'name': 'Служба спасения', 'phone': '911'},
#     {'name': 'Пожарная служба', 'phone': '101'}
# ]
#
#
# def delete():
#     name = input(f'{contacts}\nname:')
#
#     for contact in contacts:
#         if name == contact['name']:
#             contacts.remove(contact)
#
#
# delete()
#
#
# def edit():
#     name = input(f'{contacts}\nname:')
#
#     for contact in contacts:
#         if name == contact['name']:
#             new_name = input('new_name:')
#             new_phone = input('new_phone:')
#             contact.update(name=new_name, phone=new_phone)
#     print(contacts)
#
#
# edit()


# def create():
#
#     # new_name = input('new name')
#     # new_phone = input('new phone')
#     # contacts.append({'name': new_name, 'phone': new_phone})
#
#
# create()
# print(contacts)


# def find_contact(name, phone):
#     if name in contacts.keys():
#         return True
#     if phone in contacts.keys():
#         return True
#     return False
#
#
# def add(name: str, phone: int):
#     if name not in contacts.keys():
#         if phone in range(1, 15):
#             contacts [name] = phone
#     else:
#         print(f'{name} такое имя есть!')
#
#
# def delete(name):
#     if name in contacts.keys():
#         del contacts[name]
#     else:
#         print(f'{name} такого имени нет!')
#
#
# delete()
#
# def edit(name, new_name, phone):
#     if name in contacts.keys():
#         contacts[new_name] = contacts.pop(name)
#     if phone in contacts.keys():
#         contacts[new_phone] = contacts.pop(phone)
#
# while True:
#     print(contacts)
#     command = input(f'1) add\n'
#                     f'2) edit\n'
#                     f'3) delete\n')
#     if command == '1':
#         add(name=input('новое имя: '), phone=int(input('номер:')))
#     elif command == '2':
#         edit(name=input('старое имя: '), new_name=input('новое имя: '), phone=input('новый номер'))
#     elif command == '3':
#         delete(name=input('старое имя: '))
#     else:
#         print('Такого выбора нет.')
#
# print(contacts)
