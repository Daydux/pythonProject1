day = int(input('Enter your birthday: '))
month = int(input('Enter your birth month: '))

if day >= 23 <= 31 and month == 12 or day >= 1 <= 20 and month == 1:
    print("Козерог")

elif day >= 23 <= 30 and month == 11 or day >= 1 <= 22 and month == 12:
    print("Стрелец")

elif day >= 24 <= 31 and month == 10 or day >= 1 <= 22 and month == 11:
    print("Скорпион")

elif day >= 24 <= 30 and month == 9 or day >= 1 <= 23 and month == 10:
    print("Весы")

elif day >= 22 <= 31 and month == 8 or day >= 1 <= 23 and month == 9:
    print("Дева")

elif day >= 23 <= 31 and month == 7 or day >= 1 <= 21 and month == 8:
    print("Лев")

elif day >= 22 <= 30 and month == 6 or day >= 1 <= 22 and month == 7:
    print("Рак")

elif day >= 22 <= 31 and month == 5 or day >= 1 <= 21 and month == 6:
    print("Близнецы")

elif day >= 21 <= 30 and month == 4 or day >= 1 <= 21 and month == 5:
    print("Телец")

elif day >= 21 <= 31 and month == 3 or day >= 1 <= 20 and month == 4:
    print("Овен")

elif day >= 20 <= 28 and month == 2 or day >= 20 <= 29 and month == 2:
    print("Рыбы")

elif day >= 21 <= 31 and month == 1 or day >= 1 <= 19 and month == 2:
    print("Водолей")

else:
    print("Такой даты не существует")