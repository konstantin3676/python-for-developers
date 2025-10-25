from typing import NoReturn

class CustomError(Exception):
    pass

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.stock = quantity

    def update_stock(self, quantity: int) -> NoReturn:
        new_quantity = self.stock + quantity
        if new_quantity < 0:
            raise CustomError(f"Недостаточно товара '{self.name}' на складе для выполнения операции")
        self.stock = new_quantity

class Order:
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product, quantity: int) -> NoReturn:
        if product.stock < quantity:
            raise CustomError(f"Недостаточно товара '{product.name}' на складе. Доступно: {product.stock}")
        self.products[product] = self.products.get(product, 0) + quantity
        product.update_stock(-quantity)
    
    def calculate_total(self) -> float:
        total = 0.0
        for product, quantity in self.products.items():
            total += product.price * quantity
        return total
    
    def remove_product(self, product: Product, quantity: int) -> NoReturn:
        if (quantity > self.products[product]):
            raise CustomError(f"В заказе недостаточно товара '{product.name}'. Заказано: {self.products[product]}")
        self.products[product] -= quantity
        product.update_stock(quantity)
        if self.products[product] == 0:
            del self.products[product]

    def return_product(self, product: Product, quantity: int) -> NoReturn:
        self.remove_product(product, quantity)

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product) -> NoReturn:
        self.products.append(product)

    def list_products(self) -> NoReturn:
        if not self.products:
            print('В магазине нет товаров')
            return
        print('Товары в магазине:')
        for i, product in enumerate(self.products, 1):
            print(f"{i}. {product.name} - цена: {product.price}, на складе: {product.stock}")
    
    def create_order(self) -> Order:
        return Order()
    
# Создаем магазин
store = Store()

# Создаем товары
product1 = Product("Ноутбук", 1000, 5)
product2 = Product("Смартфон", 500, 10)

# Добавляем товары в магазин
store.add_product(product1)
store.add_product(product2)

# Список всех товаров
store.list_products()

# Создаем заказ
order = store.create_order()

# Добавляем товары в заказ
order.add_product(product1, 2)
order.add_product(product2, 3)

# Изменяем количество товара в заказе
order.remove_product(product2, 1)

# Возврат товара
order.return_product(product1, 2)

# Выводим общую стоимость заказа
total = order.calculate_total()
print(f"Общая стоимость заказа: {total}")

# Проверяем остатки на складе после заказа
store.list_products()
