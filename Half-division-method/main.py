import os
from math import *

def get_count_of_digits_after_comma(number):
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0

# Функция, для обработки методом половинного деления
def function(x):
    y = sin(x)
    return y

print("\t\t\t Метод половинного деления")

print("\t Ввод диапозона х для функции y = F(x):")
min_x = float(input("Введите начальное значение x: "))
max_x = float(input("Введите конечное значение x: "))

accuracy = float(input("Введите точность нахождения x (например = 0.01): "))

def half_division(min_x, max_x, accuracy):
    x = 0 # ~ значение координаты х, при котором заданная функция у = 0 #TODO: Можно без этой переменной?
    x_range_len = float(abs(max_x - min_x)) # Длина промежутка по оси х

    # Вычисление координат y на гранциах заданного промежутка
    min_y = function(min_x)
    max_y = function(max_x)

    if not (min_y < 0 and max_y > 0 or min_y > 0 and max_y < 0):
        print("Некорректные входные данные!")
        print("Функция не имеет разные знаки на концах промежутка!")
        return -1
    
    if x_range_len <= 2 * accuracy:
        print("Некорректные входные данные!")
        print("Заданный диапозон х <= 2 * точность вычислений!")
        return -1


    while x_range_len > 2 * accuracy:
        min_y = function(min_x)
        max_y = function(max_x)

        # Вычисление координат точки середины промежутка по оси х
        mid_x = (min_x + max_x) / 2
        mid_y = function(mid_x)

        # Проверка, что знаки функции в нижней границе диапозона и его середине различны
        if min_y < 0 and mid_y > 0 or min_y > 0 and mid_y < 0:
            # Переход к левому диапозону
            max_x = mid_x
            max_y = mid_y

        else:
            # Переход к правому диапозону
            min_x = mid_x
            min_y = function(mid_x)

        x = mid_x # Текущее значение х
        x_range_len = float(abs(max_x - min_x))

    mid_x = round(mid_x, get_count_of_digits_after_comma(accuracy))

    print("При заданной функции y = 0")
    print("В точке с координатой х ~ " + str(x))
    print("Точность вычисления х = " + str(accuracy))


os.system("cls")
half_division(min_x, max_x, accuracy)

# Тестовые функциии
# formula = "(0.5 * x + 1)**2 - 6" # Формула изучаемой функции 1
# formula = "(x)**2 + 5 * x + 6" # Формула изучаемой функции 2
# formula = "(x)**2 + 2 * x + 1" # Формула изучаемой функции 3
# formula = "-(x)**2 - 5 * x + 6" # Формула изучаемой функции 4
# formula = "sin(x) + 2 * x + 1" # Формула изучаемой функции 5

# Результаты работы на тестовых функциях
# Формула 1. Ответ = 2.9 Промежуток (-2; 4)             Результат - верно
# Формула 2. Ответ = -2  Промежуток (-2.4; -1)          Результат - верно
# Формула 3. Ответ = некор. данные Промежуток(-2.4; -1) Результат - верно
# Формула 4. Ответ = 1   Промежуток(-2; 2)              Результат - неверный
# Формула 5. Ответ = 

# Проверка работы метода на тестовых функциях
# https://planetcalc.ru/3718/?type=x&x0=-2&formula=(0.5*x%2B1)%5E2-6&x1=4&epsilon=0.01    - выполнение рассчётов 1  
# https://planetcalc.ru/3718/?type=x&x0=-2.4&formula=(x)%5E2%2B5*x%2B6&x1=-1&epsilon=0.01 - выполнение рассчётов 2  
# https://planetcalc.ru/3718/?type=x&x0=10&formula=(x)%5E2%2B2*x%2B1&x1=15&epsilon=0.01   - выполнение рассчётов 3  
# https://planetcalc.ru/3718/?type=x&x0=-2&formula=-1*(x)%5E2-5*x%2B6&x1=2&epsilon=0.01   - выполнение рассчётов 4  

