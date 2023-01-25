# rounds = 5
# while rounds > 0:
#         print(rounds)
#         rounds -= 1


# c = 0
# while c < 50:
#     if c == 10:
#         break
#     print('hello', c)
#     c -= 1

# c = 0
# while c < 50:
#     c += 1
#     if c == 10:
#         #break
#         continue
#     print('hello', c)

# c = 0
# while c < 50:
#     c += 1
#     if c % 2 == 0:
#         continue
#     print('hello', c)

# while True:
#     time = input('введите время: ').lower()
#     if time == 'morning' or time == 'утро':
#         print('good morning')
#     elif time == 'day' or time == 'день':
#         print('good afternoon')
#     elif time == 'evening' or time == 'вечер':
#         print('good evening')
#     else:
#         print('hello')


# i - iterable, item

# если наоборот, то  word[::-1]

# word = 'python'

# for letter in word:word[::-1]
#     if letter == 'h':
#         #break
#         continue
#     print(letter)


# for number in range(1, 11):
#     if number % 2 == 0:
#         print(number)

# for i in range(1, 4):
#     for k in range(1, 4):
#         print(i, k)


# cash = 1000000
# percents = 0.1
# years = 10


# for i in range(1, years+1):
#     cash += cash * percents
#     print(f'год: {i} >> {cash}')


eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
rus = "йцукенгшщзхъфывапролджэячсмитьбю"

# print (len(eng),len(rus))

while True:
    word = input(' \nвведите слово: ').lower()
    if word == 'exit':
        print('exit...')
        break
    for i in word:
        if i in rus:
            print(eng[rus.index(i)], end='')
        else:
            print(rus[eng.index(i)], end='')

eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
rus = "йцукенгшщзхъфывапролджэячсмитьбю"

while True:
    word = input('\nвведите слово: ').lower()
    if word == 'выход':
        print('exit...')
        break
    for i in word:
        if i in rus:
            print(eng[rus.index(i)], end='')
        else:
            print(rus[eng.index(i)], end='')

# for i in 'python':
#     if i == 't':
#         break
# else:
#     print('Весь цикл сработал')
