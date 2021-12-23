import os

# Алгоритм метода левых/правых прямоугольников с автоматическим выбором шага

def calculate_area(x, function):
    return eval(function.replace('x', str(x)))

os.system("cls")

print("\t\t\t Приближенное вычисление площади фигуры под графиком методом левых прямоугольников")

print("\t Ввод интервала на котором вычисляется площадь фигуры: ")
min_x = int(input("Введите начальное значение x: ")) # a = 1
max_x = int(input("Введите конечное значение x: ")) # b = 2

accuracy = float(input("Введите точность вычислений (пример = 0.01): ")) # accuracy = 0.0001

print("\t Выбор метода решения прямоугольниками: ")
method = int(input("Введите 0 - левыми, 1 - правыми: ")) # c = 0

# Заданная функция
func = '(2*x - 2)'

RECTANGLES_AMOUNT = rectangles_amount = 1 # (потом будет удваиваться) # N n
prev_integral = 0 # s1
cur_integral = 1  # s (1, чтобы было больше prev_integral и цикл запустился) 
rectangle_width = 0

while abs(cur_integral - prev_integral) > accuracy: # Остановка расчётов по достижению заданной точности
    prev_integral = cur_integral 
    rectangles_amount = RECTANGLES_AMOUNT = 2*RECTANGLES_AMOUNT # Удвоение кол. прямоугольников

    rectangle_width = (max_x-min_x) / rectangles_amount # Опр. ширины прямоугольников

    x = min_x + method*rectangle_width # Опр. x в зависимости от выбранного метода
    cur_integral = 0

    while rectangles_amount > 0:
        rectangles_amount -= 1
        F = calculate_area(x, func)
        cur_integral += F
        x += rectangle_width
    cur_integral = abs(cur_integral*rectangle_width)

print(f"Итоговое кол. прямоугольников, на которое была поделена фигура под графиком = {rectangles_amount}")
print(f"Площадь фигуры под графиком = {cur_integral}")
print(f"Округленная площадь фигуры под графиком = {round(cur_integral)}")
