def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()



test_function()
#inner_function() #будет ошибка, т.к. эта функция находится только в облсти видимости test_function