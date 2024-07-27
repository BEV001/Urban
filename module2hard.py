#module2hard

number =int(input("Введите число от 3 до 20: "))
input("Нажмите enter для подбора пароля! ")
results = ''
for first_number in range(1,number):
    for second_number in range(first_number+1,number):
        if number % (first_number+second_number) == 0:
            results += str(first_number)+str(second_number)
        else:
            continue
print("Пароль: ", results)