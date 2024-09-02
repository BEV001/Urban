#Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции"

def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    incorrect_numbers = []
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Переданный элемент: "{i}" - явлется некорректным тип данном данных для подсчетов')
            incorrect_numbers.append(i)

    return (result,incorrect_data)

def calculate_average(numbers):
    try:
        results = personal_sum(numbers)
        sum = results[0]
        len_ = len(numbers) - results[1]
        average = sum / len_
    except ZeroDivisionError:
        average = 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        average = None

    return average

print(f'Результат 1: {personal_sum([1,"2", 3])}')
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать