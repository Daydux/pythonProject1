while True:
    word = input("Введите слово: ")
    glasnye = 0
    soglasnye = 0
    if word == 'exit':
        print('exit...')
        break
    elif word == 'выход':
        print("exit...")
        break

    for i in word:
        letter = i.lower()
        if letter == "a" or letter == "e" or \
                letter == "i" or letter == "o" or \
                letter == "u" or letter == "y" or \
                letter == "и" or letter == "ё" or \
                letter == "ы" or letter == "э" or \
                letter == "я" or letter == "ю" or \
                letter == "а" or letter == "у" or \
                letter == "о" or letter == "е":
            glasnye += 1
        else:
            soglasnye += 1

    print("Слово:", word)
    print("Количество букв: ", len(word))
    print("Гласных:", glasnye)
    print("Согласных", soglasnye)
    glasnye = round(glasnye / len(word) * 100, 2)
    print("Гласные", glasnye, '%')
    print("Согласные", round(100 - glasnye, 2), '%')
