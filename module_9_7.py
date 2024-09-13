def is_prime(func):
    def wrapped(*args):
        number = func(*args)
        i = 2
        while number % i != 0 and i <= number:
            i += 1
        if i == number:
            print("Простое")
        else:
            print("Составное")
        return number

    return wrapped


@is_prime
def sum_three(*args):
    sum_result = 0
    for i in args:
        sum_result += i
    return sum_result


result = sum_three(2, 3, 6)
print(result)