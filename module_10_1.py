from time import sleep
from datetime import datetime
from threading import Thread



def write_words(word_count, file_name):
    with open(file_name, 'a+', encoding='utf-8') as file:
        for i in range(1, word_count+1):
            text = "Какое-то слово №"+str(i)+'\n'
            file.write(text)
            sleep(0.1)
    return print(f'Завершилась запись в файл {file_name}')


start_1 = datetime.now()
first = write_words(10, 'example1.txt')
second = write_words(30, 'example2.txt')
third = write_words(200, 'example3.txt')
fourth = write_words(100, 'example4.txt')
stop_1 = datetime.now()
print("Время работы обычной программы:", stop_1-start_1)

start_2 = datetime.now()
first_thread = Thread(target=write_words, args=(10, 'example1_threading.txt', ))
second_thread = Thread(target=write_words, args=(30, 'example2_threading.txt', ))
third_thread = Thread(target=write_words, args=(200, 'example3_threading.txt', ))
fourth_thread = Thread(target=write_words, args=(100, 'example4_threading.txt', ))

first_thread.start()
second_thread.start()
third_thread.start()
fourth_thread.start()

first_thread.join()
second_thread.join()
third_thread.join()
fourth_thread.join()

stop_2 = datetime.now()
print("Время работы поточной программы:", stop_2-start_2)