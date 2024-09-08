first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
print(list(first_result))

second_results = (True if len(first[i]) == len(second[i]) else False for i in range(len(first)) if
                  len(first) == len(second))
print(list(second_results))
