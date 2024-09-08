# first task
import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

first_results = map(lambda x, y: True if x == y else False, first, second)
print(list(first_results))


# second task
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a+', encoding='utf-8') as file:
            for item in data_set:
                file.write(str(item) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
with open('example.txt', 'r', encoding='utf-8') as file:
        print(file.read())


# third task
class MysticBall():
    def __init__(self, *word):
        self.word = list(word)

    def __call__(self):
        return random.choice(self.word)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
