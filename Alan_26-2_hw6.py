def first_word(word):
    if type(word) == str:
        return word.split()[0]
    return False


def average(*args: float):
    a = (len(args))
    return round(sum(args) / a, 0)


def ps_check(password):
    lower_letters = 'qwertyuiopasdfghjklzxcvbnm'
    upper_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    numbers = '1234567890'
    other = "~ ` ! @ # $ % ^ & * ( ) _ - = + | \ ] } { [ ' , ; / ? . < >"
    ll = ul = num = False
    if len(password) >= 6:
        for i in password:
            if i in lower_letters:
                ll = True
            if i in upper_letters:
                ul = True
            if i in numbers:
                num = True
            if i in other:
                return False
    return ll or ul and num


print(first_word('Hello World'))
print(average(12, 16, 19, 21, 32))
print(ps_check('"kdcmck232"'))
