import  inspect
def introspection_info(obj):
    #Тип объекта
    obj_type = type(obj).__name__

    #Список всех атрибутов и методов объекта
    all_attributes_methods = dir(obj)

    #Атрибуты
    attributes = [attr for attr in all_attributes_methods if not callable(getattr(obj, attr))]
    #Методы
    methods = [method for method in all_attributes_methods if callable(getattr(obj, method))]

    # Модуль
    if hasattr(obj, '__module__'):
        module = obj.__module__
    else:
        module = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else 'builtins'


    result = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    return result



number_info = introspection_info(42)
for key, item in number_info.items():
    print(key, ':', item)

