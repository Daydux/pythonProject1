low = 1
high = 100
tries = 1
with open('results.txt', 'w') as file:
    while True:
        mid = (low + high) // 2
        is_answer = input(f'Ваше число: {mid}? (да, < или > ?)')
        if is_answer.lower() == 'да':
            print('Я угадал.')
            break
        elif is_answer == '>':
            low = mid + 1
            tries += 1
        elif is_answer == '<':
            high = mid - 1
            tries += 1
        else:
            print('Введите < или > или да ')

    user_number = str(mid)
    tries = str(tries)
    file.write(f'Угаданное число = {user_number}\n')
    file.write(f'Количество попыток = {tries}')

file = open('results.txt', 'a')
if is_answer.lower() == 'да' and tries == 1:
    file.write(f'{mid} = 50')
else:
    print()
file.close()

file = open('results.txt', 'a')
if is_answer.lower() == '>':
    file.write(f'{user_number} > {mid}')
elif is_answer.lower() == '<':
    file.write(f'{user_number} < {mid}')
else:
    print()
file.close()

# Я не понял почему не пополняется список, когда читаю код, должно всё получатся, но чего-то не выходит