def convert_to_float(string):
    try:
        numder = float(string)
    except ValueError:
        print("Строку невозможно преобразовать в число")

string = input('Введите строку: ')
convert_to_float(string)