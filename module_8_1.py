#Домашнее задание по уроку "Try и Except".

def add_everything_up(a, b):
    print("-------------")
    try:
        print("{a:.3f} + {b:.3f} = {result:.3f}".format(a=a, b=b, result=a+b))

    except TypeError as exc:
        print(f'Одна из переменных не явлеется числом')
        print(f"{a} + {b} = {str(a)+str(b)}")
    else:
        print("Сложение возможно и было выполнено верно")
    finally:
        print("Задание выполнено!")



add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)
