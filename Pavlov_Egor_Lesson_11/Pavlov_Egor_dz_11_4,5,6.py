class MyError(Exception):
    @staticmethod
    def only_int(data):
        if data.price[0] == '-' or data.price[0] == '+' or data.price.isdigit():
            for i in range(1, len(data.price)):
                if data.price[i].isdigit():
                    pass
                else:
                    print('Ошибка! Нужно вводить число.')
                    return False
        else:
            print('Ошибка! Нужно вводить число.')


class OfficeEquipWarehouse:
    def __init__(self, name):
        self.name = name
        self.stock = {}
        print(f'Склад {name} создан')

    def take_to_warehouse(self, item):
        stock_price = self.stock.get(item.model, [0, 0])[0]
        stock_vol = self.stock.get(item.model, [0, 0])[1]
        new_stock_price = stock_price + item.price
        new_stock_vol = stock_vol + 1
        if self.stock.get(item.model) is None:
            self.stock.setdefault(item.model, [new_stock_price, new_stock_vol])
        else:
            self.stock.pop(item.model)
            self.stock.setdefault(item.model, [new_stock_price, new_stock_vol])
        print(f'Товар принят на склад')

    def get_stock(self, *args):
        for name in args:
            print(f'Остаток {name} на складе: {self.stock.get(name)[1]} шт на {self.stock.get(name)[0]}')


class OfficeEquipment:
    def __init__(self, name, purchase_price, added_value=0.1):  # warehouse='self', method_of_admission='purchase'):
        self.equipment = str(name)
        self.price = float(purchase_price)
        self.added_value = float(added_value)
        # self.wh = warehouse
        # self.method = method_of_admission
        self.stock_number = 0


class Printer(OfficeEquipment):
    def __init__(self, name,
                 purchase_price,
                 model,
                 prt_speed,
                 added_value=0.2):  # другая наценка
        super().__init__(name, purchase_price, added_value)
        self.model = str(model)
        self.invent_numb = 0
        self.prt_speed = str(prt_speed)
        print('Принтер создан')


class Scanner(OfficeEquipment):
    def __init__(self, name,
                 purchase_price,
                 model,
                 glass_size,
                 added_value=0.1):
        super().__init__(name, purchase_price, added_value)
        self.model = str(model)
        self.invent_numb = 0
        self.glass_size = int(glass_size)
        print('Сканер создан')


class Copier(OfficeEquipment):
    def __init__(self, name,
                 purchase_price,
                 model,
                 colour,
                 added_value=0.1):
        super().__init__(name, purchase_price, added_value)
        self.model = str(model)
        self.invent_numb = 0
        self.colour = bool(colour)
        print('Копир создан')


warehouse1 = OfficeEquipWarehouse('warehouse1')
a = Printer('Printer', 120, 'speedy200', '200 per min')
b = Printer('Printer', 100, 'speedy200', '180 per min')
warehouse1.take_to_warehouse(a)
warehouse1.take_to_warehouse(b)
warehouse1.get_stock(a.model)
c = Scanner('Scanner', 15, 'old_scrap', 4)
warehouse1.take_to_warehouse(c)
warehouse1.get_stock(a.model, c.model)
