import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)

            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")
            # Задерживаем на короткое время
            time.sleep(0.001)


            # Проверяем условие для разблокировки
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()




    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            #self.lock.acquire()
            print(f" Запрос на {amount}")
            if amount <= self.balance:
                self.balance -= amount
                print(f" Снятие: {amount}. Баланс: {self.balance}")
                #self.lock.release()

            else:
                print(" Запрос отклонён, недостаточно средств")
                self.lock.acquire()






# Создаем объект класса Bank
bk = Bank()

# Создаем потоки для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запускаем потоки
th1.start()
th2.start()

# Ожидаем завершения выполнения потоков
th1.join()
th2.join()

# Выводим итоговый баланс
print(f'Итоговый баланс: {bk.balance}')
