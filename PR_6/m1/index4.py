import functools
import random

def io(*args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*wrapper_args, **wrapper_kwargs):
            input_data = []
            for arg_func in args[:-1]:
                input_data.append(arg_func())
            result = func(*input_data, *wrapper_args, **wrapper_kwargs)
            args[-1](result)
            return result
        return wrapper
    return decorator

if __name__ == "__main__":
    @io(input, input, input, print)
    def f1(x, y, z):
        return x + y + z

    f1()

    @io(lambda: random.random(), lambda: random.random(), lambda x: x)
    def f2(x, y):
        return x * y

    print(f2())