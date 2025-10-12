def calc_order_cost(data_path):
    with open(data_path, 'r') as data:
        order_cost = 0
        for order_string in data.readlines():
            order_item = order_string.split()
            order_cost += int(order_item[1]) * int(order_item[2])
        print(order_cost)

calc_order_cost('homework-2/prices.txt')