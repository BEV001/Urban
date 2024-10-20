from queue import Queue
from threading import Thread
from random import randint
from time import sleep
class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        waiting_time = randint(3,10)
        sleep(waiting_time)


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables) #Class Table

    def guest_arrival(self, *guests):

        for guest in guests:
            seated = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} took Table {table.number}')
                    seated = True
                    break
            if not seated:
                self.queue.put(guest)
                print(f'{guest.name} is in line')


    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f' {table.guest.name} finished eating and left')
                    print(f' Table {table.number} is free')
                    table.guest = None

                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        print(f'{table.guest.name} was out line and took Table {table.number}')
                        table.guest.start() #start Thread



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()




