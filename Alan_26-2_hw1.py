a = float(input('Укажите сколько градусов цельсия в Чуйской области: '))
b = float(input('Укажите сколько градусов цельсия в Ошской области: '))
c = float(input('Укажите сколько градусов цельсия в Нарынской области: '))
d = float(input('Укажите сколько градусов цельсия в Баткенской области: '))
e = float(input('Укажите сколько градусов цельсия в Таласской области: '))
f = float(input('Укажите сколько градусов цельсия в Жалал-Абадской области: '))
g = float(input('Укажите сколько градусов цельсия в Каракольской области: '))
sum_all = a + b + c + d + e + f + g
average_degrees = sum_all / 7
average_degrees = round(average_degrees, 1)
print (f'Средний показатель температуры воздуха по КР на сегодня {average_degrees} °C.')