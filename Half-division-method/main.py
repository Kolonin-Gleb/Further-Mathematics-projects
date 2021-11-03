import os

def get_count_of_digits_after_comma(number):
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0

os.system("cls")

def half_division():
    ### Получение входных данных

    print("\t\t\t Метод половинного деления")
    # Тестовые функциии
    #formula = "(0.5 * x + 1)**2 - 6" # Формула изучаемой функции 1
    #formula = "(x)**2 + 5 * x + 6" # Формула изучаемой функции 2
    formula = "(x)**2 + 2 * x + 1" # Формула изучаемой функции 3
    #formula = "-(x)**2 - 5 * x + 6" # Формула изучаемой функции 4

    x = 0 # ~ значение координаты х, при которой заданная функция у = 0

    print("\t Ввод диапозона х для функции y = F(x):")
    min_x = float(input("Введите начальное значение x: "))
    max_x = float(input("Введите конечное значение x: "))

    accuracy = float(input("Введите точность, нахождения x (пример = 0.01): "))

    x_range_len = float(abs(max_x - min_x)) # Длина промежутка по оси х

    ### Проверка на разность знаков функции на концах промежутка

    # Вычисление координат y на гранциах заданного промежутка
    min_y = formula.replace('x', str(min_x))
    min_y = eval(min_y)
    max_y = formula.replace('x', str(max_x))
    max_y = eval(max_y)

    if not (min_y < 0 and max_y > 0 or min_y > 0 and max_y < 0):
        print("Некорректные входные данные!")
        print("Функция не имеет разные знаки на концах промежутка!")
        return -1

    ### Запуск вычислений

    while x_range_len > 2 * accuracy:
        min_y = formula.replace('x', str(min_x))
        min_y = eval(min_y)
        max_y = formula.replace('x', str(max_x))
        max_y = eval(max_y)

        # Ищем координаты точки середины промежутка по оси х
        mid_x = (min_x + max_x) / 2
        mid_y = formula.replace('x', str(mid_x))
        mid_y = eval(mid_y)

        # Проверка, что знаки функции в нижней границе диапозона и его середине различны
        if min_y < 0 and mid_y > 0 or min_y > 0 and mid_y < 0:
            # Переходим к левому диапозону
            max_x = mid_x
            max_y = mid_y

        else:
            # Переходим к правому диапозону
            min_x = mid_x
            min_y = formula.replace('x', str(mid_x))
            min_y = eval(min_y)

        x = (min_x + max_x) / 2
        x_range_len = float(abs(max_x - min_x))

    x = round(x, get_count_of_digits_after_comma(accuracy))

    print("Функция y = " + str(formula) + " = 0")
    print("В точке с координатой х ~ " + str(x))
    print("Точность вычисления х = " + str(accuracy))

half_division()

# Результаты работы на тестовых функциях
# Формула 1. Ответ = 2.9 Промежуток (-2; 4)             Результат - верно
# Формула 2. Ответ = -2  Промежуток (-2.4; -1)          Результат - верно
# Формула 3. Ответ = некор. данные Промежуток(-2.4; -1) Результат - верно
# Формула 4. Ответ = 1   Промежуток(-2; 2)              Результат - неверный

# Проверка работы метода на тестовых функциях
# https://planetcalc.ru/3718/?type=x&x0=-2&formula=(0.5*x%2B1)%5E2-6&x1=4&epsilon=0.01    - выполнение рассчётов 1  
# https://planetcalc.ru/3718/?type=x&x0=-2.4&formula=(x)%5E2%2B5*x%2B6&x1=-1&epsilon=0.01 - выполнение рассчётов 2  
# https://planetcalc.ru/3718/?type=x&x0=10&formula=(x)%5E2%2B2*x%2B1&x1=15&epsilon=0.01   - выполнение рассчётов 3  
# https://planetcalc.ru/3718/?type=x&x0=-2&formula=-1*(x)%5E2-5*x%2B6&x1=2&epsilon=0.01   - выполнение рассчётов 4  