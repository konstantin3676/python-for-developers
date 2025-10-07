import math

def calc_sqrt(number):
    try:
        result = math.sqrt(number)
        print(result)
    except ImportError:
        print('Модуль math не импортирован')
    except ValueError:
        print('Невозможно извлечь корень из отрицательного числа')

number = int(input('Введите число: '))
calc_sqrt(number)