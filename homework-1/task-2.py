try:
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    result = num_1 / num_2
    print(result)
except ValueError:
    print('Значение должно быть числом')
except ZeroDivisionError:
    print('Деление на ноль невозможно')
