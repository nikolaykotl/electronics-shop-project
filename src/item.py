import os
import csv
import sys

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []



    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price
    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.pay_rate * self.price
        return self.price

    # Геттер для name
    @property
    def name(self):
        return self.__name

    #Сеттер для name
    @name.setter
    def name(self, value: str):
        if len(value) <= 10:
            self.__name = value
        else:
            self.__name = value[0:10]


    @classmethod
    def instantiate_from_csv(cls):
        #создает путь к файлу \src\items.csv
        path_dir = os.path.dirname(sys.argv[0])
        s = path_dir
        pth_file = s[:s.rindex("\\") + 1]
        path_file = pth_file +'\src\items.csv'
        #читаем файл
        with open(path_file, 'r', encoding= 'utf8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name, price, quantity = row['name'], row['price'], row['quantity']
                item = cls(name, price, quantity)
                Item.all.append(item)

    @staticmethod
    def string_to_number(s):
        s = str(len(Item.all))
        return int(s)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'