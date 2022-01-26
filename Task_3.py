from functools import wraps


def logger(callback):
    @wraps(callback)
    def wrapper(*args):
        func_result = callback(*args)
        log_result = tuple(f'{arg}: {type(arg)}' for arg in args)
        print(f'{callback.__name__}{log_result}')
        print(type(func_result))
        return func_result

    return wrapper


@logger
def calc_cube(x, y, z):
    return x * y * z


result = calc_cube(3, 5.6, 6)
print(result)
