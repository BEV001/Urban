def custom_write(file_name, strings):
    file = open(file_name, 'a+',  encoding='utf-8')
    results = {}

    for string in strings:
        file.seek(0)
        number_str = file.read().count('\n')+1
        key = tuple([number_str, file.tell()])
        file.write(string)
        file.write('\n')
        results.update({key: string})

    file.close()
    return results


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
file_name = 'module_7_2.txt'

results = custom_write(file_name, info)
for elem in results.items():
  print(*elem)
