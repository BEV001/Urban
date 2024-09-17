
from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = 100
        count_days = 0
        while enemies > 0:
            if enemies >= self.power:
                enemies -= self.power
            else:
                enemies = 0
            count_days += 1
            sleep(0.1)
            if count_days == 1:
                print(f"{self.name},сражается {count_days} день, осталось {enemies} врагов.")
            elif count_days <= 4:
                print(f"{self.name},сражается {count_days} дня, осталось {enemies} врагов.")
            else:
                print(f"{self.name},сражается {count_days} дней, осталось {enemies} врагов.")

        if count_days == 1:
            print(f"{self.name}, одержал победу спустя  {count_days} день!")
        elif count_days <= 4:
            print(f"{self.name}, одержал победу спустя  {count_days} дня!")
        else:
            print(f"{self.name}, одержал победу спустя  {count_days} дней!")


first_knight = Knight('Sir Lancelot', 11)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")





