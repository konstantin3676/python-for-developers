import threading

def calculate_squares():
    for i in range(1, 11):
        square = i ** 2
        print(f"Квадрат {i} = {square}")

def calculate_cubes():
    for i in range(1, 11):
        cube = i ** 3
        print(f"Куб {i} = {cube}")

if __name__ == "__main__":
    thread1 = threading.Thread(target=calculate_squares)
    thread2 = threading.Thread(target=calculate_cubes)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()