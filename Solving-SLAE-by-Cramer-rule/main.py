# Решение СЛАУ методом Крамера
# Решение СЛАУ методом Крамера, если СЛАУ имеет 1 решение. Иначе будет выдан ответ: Решений нет или их бесконечно много.

import numpy as np # Для работы с матрицами
import os # Для чистки экрана

os.system('cls||clear')

print("\t\t Ввод основной матрицы")
print("Введите 3 коэффициента первой строки через пробел:")
a1, b1, c1 = input().split(' ')

print("Введите 3 коэффициента второй строки через пробел:")
a2, b2, c2 = input().split(' ')

print("Введите 3 коэффициента третьей строки через пробел:")
a3, b3, c3 = input().split(' ')

# Создание основной матрицы
A = np.matrix(f'{a1} {b1} {c1}; {a2} {b2} {c2}; {a3} {b3} {c3}')

print("Введенная вами матрица:")
print(A)

print("\t\t Ввод свободных коэффициентов")
print("Введите 3 коэффициента через пробел")
k1, k2, k3 = input().split(' ')

input("Нажмите Enter для продолжения:")
os.system('cls||clear')

                     # Поиск определителей

detA = round(np.linalg.det(A))
print(detA)

# Поочередная замена столбцов на столбец свободных коэффициентов
A = np.matrix(f'{k1} {b1} {c1}; {k2} {b2} {c2}; {k3} {b3} {c3}')
detA1 = round(np.linalg.det(A))

A = np.matrix(f'{a1} {k1} {c1}; {a2} {k2} {c2}; {a3} {k3} {c3}')
detA2 = round(np.linalg.det(A))

A = np.matrix(f'{a1} {b1} {k1}; {a2} {b2} {k2}; {a3} {b3} {k3}')
detA3 = round(np.linalg.det(A))

                     # Решение СЛАУ

os.system('cls||clear')

if detA == 0:
    print("Ответ: Решений нет или их бесконечно много")
else:
    x = detA1 / detA
    y = detA2 / detA
    z = detA3 / detA

    print(f"Ответ: ({x}; {y}; {z})")

