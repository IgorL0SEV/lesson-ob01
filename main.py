
# 1. Создай класс `Store`:
# -Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
# - Методы класса:
# - `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
# -  метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# - метод для обновления цены товара.
#
# 2. Создай несколько объектов класса `Store`:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.



class Store:
    def __init__(self, name_store, address_store):
        self.name_store = name_store
        self.address_store = address_store
        self.items = {}

    def add_item (self, item_name, item_price):
        self.items [item_name] = item_price

    def add_new_item (self, item_name, item_price):
        self.items [item_name] = item_price
        print(f"Внимание, новинка! Товар {item_name} появился в магазине {self.name_store} по цене {item_price} руб.")
        print("")

    def del_item (self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} выведен из ассортимента магазина {self.name_store}.")
            print("")
        else:
            print (f"Товар {item_name} не найден в магазине {self.name_store}.")

    def price_item(self, item_name):
        if item_name in self.items:
            print (f"Цена на товар {item_name} равна {self.items[item_name]} рублей.")
        else:
            print (f"Товар {item_name} не найден в магазине {self.name_store}.")
            print ("None")

    def new_price_item(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print (f"Цена на товар {item_name} изменилась, теперь она равна {self.items[item_name]} рублей.")
        else:
            print (f"Товар {item_name} не найден в магазине {self.name_store}.")

    def show_store_items (self):
        print (f"Магазин {self.name_store}, по адресу {self.address_store}.")
        print("В наличии следующий товар: ")
        for k, v in self.items.items():
            print (f"{k} по цене : {v} руб.")
        print("")


store_1 = Store("<ГАСТРОНОМ_1>", "Прохладная д.5")
store_2 = Store("<УНИВЕРСАМ_2>", "Южная д.19")
store_3 = Store("<ХЛЕБНЫЙ_3>", "Северная д.25")

store_1.add_item("Пряник", 50.00)
store_1.add_item("Газировка", 20.00)
store_1.add_item("Молоко", 15.00)

store_2.add_item("Пряник", 50.00)
store_2.add_item("Пельмени", 30.00)
store_2.add_item("Шоколад", 30.00)

store_3.add_item("Пельмени", 30.00)
store_3.add_item("Шоколад", 30.00)
store_3.add_item("Молоко", 15.00)

store_1.show_store_items()

store_3.show_store_items()

store_3.new_price_item("Шоколад", 100)

store_3.add_new_item("МУКА", 10.00)
store_3.show_store_items()

store_3.del_item("Пельмени")
store_3.show_store_items()