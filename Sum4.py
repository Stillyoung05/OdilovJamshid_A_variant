def check_arguments(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, str):
                return "Error: Argument should not be a string"
        result = func(*args, **kwargs)
        return result
    return wrapper


@check_arguments
def multiply_numbers(a, b):
    return a * b


result1 = multiply_numbers(2, 3)
print(result1)
result2 = multiply_numbers(2, '3')
print(result2)
