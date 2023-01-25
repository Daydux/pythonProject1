
# lambda_func = lambda a, b: a + b
#
#
# def def_func(a, b):
#     return a + b
#
#
# print(lambda_func(2, 3))
# print(def_func(2, 3))
# print(type, lambda_func)
# print(type, def_func)


# def up_letter(word):
#     return word.title()
#
#
# def show_words(func, words):
#     for word in words:
#         print(func(word))
#
#
# words = ['python', 'bishkek', 'geektech']
#
# show_words(lambda word: word.title(), words)

# show_words(up_letter, words)
# show_words(type, words)
# show_words(len, words)


# map, filter, sorted

# numbers = list(range(1, 11))
#
#new = list(map(lambda x: x*3, numbers))
# new = list(map(str, numbers))
#
#
# # print(numbers, new, sep='\n')
# print(f"{numbers}, \n {new} ")



# numbers = list(range(1, 11))
#
# # new = tuple(filter(lambda x: x > 5, numbers))
# # new = [i for i in numbers if i > 4]
# # new = sorted(numbers, key=lambda x: x % 2 == 0)
# new = sorted(numbers, key=lambda x: x % 2 == 0, reverse=True)
#
# print(numbers, new, sep='\n')
#
# result = lambda *args: sum(args) / len(args)
#
# print(result(2, 3, 4))

# try:
#     code
# except:
#     message, define smth
# finally:
#     message


# try:
#     print(2 + '2')
# except:
#     print('неверный тип данных')
# finally:


# word = 'python'
# while True:
#     try:
#         index_user = int(input('введите индекс: '))
#         print(word[index_user])
#     except:
#         print('только цифры от 0 до 5')
    # except IndexError:
    #     print('неверный индекс!')
    # except ValueError:
    #     print('только цифры!')


# def func(a,b):
#     return a+b

# assert func(2,3) == 5
# assert func(3,3)== 7, f'неправильно! func(3,3) должно вернуть {func(3,3)}'





# raise, assert
