import numpy as np

# Задание 1
# a) Создание массивов
print("Задание 1:")

array_a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Массив a:\n", array_a)
matrix_b = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9], [10.1, 11.11, 12.12], [13.13, 14.14, 15.15]])
print("Матрица b:\n", matrix_b)
array_c = np.ones(5)
print("Массив из единиц c:\n", array_c)
matrix_d = np.zeros((3, 3))
print("Матрица из нулей d:\n", matrix_d)
array_e = np.arange(0, 4.5, 0.5)
print("Диапазон значений от 0 до 4 с шагом 0.5 e:\n", array_e)
array_f = np.random.normal(size=5)
print("Массив из 5 чисел с нормальным распределением f:\n", array_f)
array_f_int32 = array_f.astype(np.int32)
print("Тип элементов массива f изменен на int32:\n", array_f_int32)
array_h = np.random.randint(low=1, high=10, size=16).reshape(4, 4)
print("Целочисленная случайная матрица h:\n", array_h)
matrix_i = np.random.random((4, 2))
print("Вещественная случайная матрица i:\n", matrix_i)

# Задание 2
# a) Создание целочисленной матрицы
print("\nЗадание 2:")

matrix_a = np.random.randint(low=1, high=10, size=(4, 4))
print("Целочисленная матрица a:\n", matrix_a)
result_aa = matrix_a + matrix_a
print("a + a:\n", result_aa)
result_am = matrix_a - matrix_a
print("a - a:\n", result_am)
result_amul = matrix_a * matrix_a
print("a * a:\n", result_amul)
result_a_div = matrix_a / matrix_a
print("a / a:\n", result_a_div)
result_a_inv = 1 / matrix_a
print("1 / a:\n", result_a_inv)
matrix_a_transpose = matrix_a.T
print("Транспонированная матрица a:\n", matrix_a_transpose)

# Задание 3
# a) Создание целочисленных матриц
print("\nЗадание 3:")

t3_matrix_c = np.random.randint(low=1, high=10, size=(3, 3))
print("Целочисленная матрица c:\n", t3_matrix_c)
t3_matrix_d = np.random.randint(low=1, high=10, size=(3, 3))
print("Целочисленная матрица d:\n", t3_matrix_d)
# b) Матричное произведение
matrix_prod = np.dot(t3_matrix_c, t3_matrix_d)
print("Матричное произведение c * d:\n", matrix_prod)
# c) Определитель и след матрицы
det_c = np.linalg.det(t3_matrix_c)
print("Определитель матрицы c:\n", det_c)
trace_c = np.trace(t3_matrix_c)
print("След матрицы c:\n", trace_c)
# d) Обратная матрица
matrix_inv_d = np.linalg.inv(t3_matrix_d)
print("Обратная матрица матрицы d:\n", matrix_inv_d)
# e) Решение системы линейных уравнений
A = np.array([[0.4253, 0.4229, 0.6959, 0.0688],
              [0.3127, 0.0942, 0.6999, 0.3196],
              [0.1615, 0.5985, 0.6385, 0.5309],
              [0.1788, 0.4709, 0.0336, 0.6544]])

b = np.array([2.0381, 4.0999, 3.5918, 4.8432])
x = np.linalg.solve(A, b)
print("Решение системы линейных уравнений:\n", x)
solution_check = np.allclose(A @ x, b)
print("Проверка решения системы линейных уравнений:", solution_check)





























