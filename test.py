while True:
    day = int(input('Enter your birthday: '))
    month = int(input('Enter your birth month: '))

    if day >= 21 <= 31 and month == 1 or day >= 1 <= 19 and month == 2:
        print("Водолей")