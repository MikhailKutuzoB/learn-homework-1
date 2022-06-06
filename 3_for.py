"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""




phones =  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

iPhone_12_total_sales = sum(phones[0]["items_sold"])
Xiaomi_Mi11_total_sales = sum(phones[1]["items_sold"])
Samsung_Galaxy_21_total_sales = sum(phones[2]["items_sold"])

iPhone_12_average_sales = iPhone_12_total_sales/len(phones[0]["items_sold"])
Xiaomi_Mi11_average_sales = Xiaomi_Mi11_total_sales/len(phones[1]["items_sold"])
Samsung_Galaxy_21_average_sales = Samsung_Galaxy_21_total_sales/len(phones[0]["items_sold"])

All_products_total_sales = iPhone_12_total_sales + Xiaomi_Mi11_total_sales + Samsung_Galaxy_21_total_sales

Count_of_all_sold_items = len(phones[0]["items_sold"]) + len(phones[1]["items_sold"]) + len(phones[2]["items_sold"])
Average_total_sales = All_products_total_sales/Count_of_all_sold_items

print('Общее количество продаж iPhone 12:', iPhone_12_total_sales) 
print('Общее количество продаж Xiaomi Mi11:', Xiaomi_Mi11_total_sales)
print('Общее количество продаж Samsung Galaxy 21:', Samsung_Galaxy_21_total_sales)

print('Cреднее количество продаж', phones[0]['product'],iPhone_12_average_sales)
print('Cреднее количество продаж', phones[1]['product'], Xiaomi_Mi11_average_sales)
print('Cреднее количество продаж', phones[2]['product'], Samsung_Galaxy_21_average_sales)

print('Cуммарное количество продаж всех товаров:', All_products_total_sales)

print('Cреднее количество продаж всех товаров:', Average_total_sales)



