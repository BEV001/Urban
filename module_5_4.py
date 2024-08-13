class House():
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Создаём новый объект
        instance = super(House, cls).__new__(cls)
        # Добавляем название в историю
        if args:
            cls.houses_history.append(args[0])
        return instance
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        # Выводим сообщение при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

print()

# Удаление объектов
del h2
del h3

print(House.houses_history)

