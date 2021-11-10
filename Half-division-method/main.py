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
    y = (0.5 * x + 1)**2 - 6
    # y = sin(x)
    return y

os.system('cls||clear')
print("\t\t\t Метод половинного деления")

print("\t Ввод диапозона х для функции y = F(x):")
min_x = float(input("Введите минимальный x: "))
max_x = float(input("Введите максимальный x: "))

accuracy = float(input("Введите точность вычисления x (например = 0.01): "))

def half_division(min_x, max_x, accuracy):
    x_range_len = float(abs(max_x - min_x)) # Длина дипозона по оси х

    # Вычисление координат y на гранциах заданного диапозона
    min_y = function(min_x)
    max_y = function(max_x)

    if (min_y * max_y > 0):
        print("Некорректные входные данные!")
        print("Функция не имеет разные знаки на концах диапозона!")
        return -1
    
    if x_range_len <= 2 * accuracy:
        print("Некорректные входные данные!")
        print("Заданный диапозон х <= 2 * точность вычислений!")
        return -1

    # Вычисление координат точки середины диапозона по оси х
    mid_x = (min_x + max_x) / 2
    mid_y = function(mid_x)

    while (mid_y < 0.001 and mid_y > -0.001): # Приблизительное равенство у = 0
        min_y = function(min_x)
        max_y = function(max_x)

        # Вычисление координат точки середины диапозона по оси х
        mid_x = (min_x + max_x) / 2
        mid_y = function(mid_x)

        # Проверка, что знаки функции в нижней границе диапозона и его середине различны
        if (min_y * max_y < 0):
            # Переход к левому диапозону
            max_x = mid_x
            max_y = mid_y
        else:
            # Переход к правому диапозону
            min_x = mid_x
            min_y = function(mid_x)

    x = x_range_len / 2
    x = round(x, get_count_of_digits_after_comma(accuracy))


    print("При заданной функции y = 0")
    print("В точке с координатой х ~ " + str(x))
    print("Точность вычисления х = " + str(accuracy))
    print("*Настоящий ответ может быть > или < на " + str(accuracy))


os.system("cls")
half_division(min_x, max_x, accuracy)

# Тестовые функциии
#1 (0.5 * x + 1)**2 - 6  # Формула изучаемой функции 1
#2 (x)**2 + 5 * x + 6    # Формула изучаемой функции 2
#3 (x)**2 + 2 * x + 1    # Формула изучаемой функции 3
#4 -(x)**2 - 5 * x + 6   # Формула изучаемой функции 4
#5 sin(x)                # Формула изучаемой функции 5

# Результаты работы на тестовых функциях:
#1 Промежуток (-2; 4)    Точность = 0.01    Ответ = 2.9            Результат - верно      
#2 Промежуток (-2.4; -1) Точность = 0.01    Ответ = -2             Результат - верно      
#3 Промежуток(-2.4; -1)  Точность = 0.01    Ответ = некор. данные  Результат - верно      
#4 Промежуток(-2; 2)     Точность = 0.01    Ответ = 1              Результат - неверный      
#5 Промежуток(-2; 2)     Точность = 0.00001 Ответ = 0              Результат - верный     +

# Проверка работы метода на тестовых функциях:
#1 https://planetcalc.ru/3718/?type=x&x0=-2&formula=(0.5*x%2B1)%5E2-6&x1=4&epsilon=0.01
#2 https://planetcalc.ru/3718/?type=x&x0=-2.4&formula=(x)%5E2%2B5*x%2B6&x1=-1&epsilon=0.01
#3 https://planetcalc.ru/3718/?type=x&x0=10&formula=(x)%5E2%2B2*x%2B1&x1=15&epsilon=0.01
#4 https://planetcalc.ru/3718/?type=x&x0=-2&formula=-1*(x)%5E2-5*x%2B6&x1=2&epsilon=0.01
#5 https://planetcalc.ru/3718/?type=x&x0=-2&formula=sin(x)&x1=2&epsilon=0.01

