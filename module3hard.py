#module3hard
def calculate_structure_sum(*args):
    result = 0
    data_ = args[0]
    if isinstance(data_, dict):
        data_ = list(data_.keys()) + list(data_.values())
        first = data_[0]
    elif isinstance(data_[0], int) or isinstance(data_[0], str):
        first = data_[0]
    elif isinstance(data_[0], dict):
        first = data_[0]
    else:
        first = list(data_[0])


    if isinstance(data_, int) or isinstance(first, float):
        result += data_
        if len(data_structure) > 1:
            data_structure.pop(0)
            return result + calculate_structure_sum(data_structure[0])
        else:
            return result
    elif isinstance(first, int) or isinstance(first, float):
        result += first

    if isinstance(data_, str):
        result += len(data_)
        if len(data_structure) > 1:
            data_structure.pop(0)
            return result + calculate_structure_sum(data_structure[0])
        else:
            return result
    elif isinstance(first, str):
        result += len(first)

    if isinstance(first, dict):
        first = list(first.keys()) + list(first.values())

    if isinstance(first, list) and len(first) != 0:
        if len(first) > 0:
            return result + calculate_structure_sum(first)
        else:
            if len(data_structure) > 1:
                data_structure.pop(0)
                return result + calculate_structure_sum(data_structure[0])
            else:
                return result

    if isinstance(data_, list) or isinstance(data_, tuple):
        if len(data_) > 1:
            return result + calculate_structure_sum(data_[1:])
        else:
            if len(data_structure) > 1:
                data_structure.pop(0)
                return result + calculate_structure_sum(data_structure[0])
            else:
                return result





data_structure = [
    [1, 2, 3], #6
   {'a': 4, 'b': 5}, #11
    (6, {'cube': 7, 'drum': 8}), #6+4+7+4+8 = 29
     "Hello", #5
   ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)