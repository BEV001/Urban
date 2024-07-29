def print_params(a = 1, b = 'строка', c = True):
    print (a,b,c)
    print("------------------------")

#part1
print_params()
print_params(3,2,1)
list_ = [1, 2, 3]
print_params(*list_)
print_params(list_)
print_params(b = 25)
print_params(c = [1, 2, 3])

#part2
values_list = [[1, 2], (False, "Hello world"), 1.0]
values_dict = {'a': [1,2],
               'b': True,
               'c': 'Hello world'}
#print_params(values_list)
print_params(*values_list)
#print_params(values_dict)
#print_params(*values_dict)
print_params(**values_dict)

#part3
values_list_2 = [0.5, "ноль целых пять десятых"]
print_params(*values_list_2, 42)

