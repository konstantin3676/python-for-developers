class EvenError(Exception):
    pass

class NegativeError(Exception):
    pass

def sum_list(int_list):
    result = 0

    for number in int_list:
        if number % 2 == 0:
                raise EvenError('В списке четное число')
        if number < 0:
                raise NegativeError('В списке отрицательное число')
        result += number

    print(f"Результат: {result}")

int_list = [-1, 3, 5]
try:
    sum_list(int_list)
except EvenError as e:
            print(e)
except NegativeError as e:
            print(e)