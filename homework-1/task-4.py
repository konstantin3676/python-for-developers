element_list = [1, 2, 3, 4, 5]

def get_element(index):
    try:
        element = element_list[index]
        print(element)
    except IndexError:
        print('Индекс выходит за пределы списка')

index = int(input('Введите индекс элемента: '))
get_element(index)