file = open('file.txt', 'w')
file.write('12344567')
file.close()

# with open('file.txt', 'x') as file:
#     file.write('\n222222222222')
with open('file.txt', 'a') as file:
    file.write('\n222222222222')

# from time import sleep
#
# with open('file.txt', 'r') as file:
#     start = 0
#     end = 4
#     while start < 18:
#         for i in file.readlines():
#             sleep(0.1)
#             print(i, end='')


    # for i in file.readlines():
    #     sleep(1)
    #     print(i, end='')
    # print(file.read())
    # print(file.readline())
    # print(file.readlines()[0])
#
# from datetime import datetime
# from random import choice, randint
# students = [2, 6, 9, 1, 3, 11]
#
# while len(students) !=0:
#     print(f'еще в живых: {students}')
#     student_id = choice(students)
#     name = input(f'name: {student_id} ')
#     start = datetime.now()
#     first = randint(1, 11)
#     second = randint(10, 100)
#     right_answer = first * second
#     user_answer = int(input(f'сколько будет {first} * {second}'))
#     end = datetime.now() - start
#     if user_answer == right_answer:
#         print(True)
#         with open('answer.txt', 'a') as file:
#             file.write(f'{name} {first} * {second} = {user_answer}'
#                        f' ({right_answer} {end.seconds} {False}\n)')
#     else:
#         print(False)
#         with open('answer.txt', 'a') as file:
#             file.write(f'{name} {first} * {second} = {user_answer}'
#                        f' ({right_answer} {end.seconds} {False}\n)')
#         students.remove(student_id)
#
#
#
#
#
#
