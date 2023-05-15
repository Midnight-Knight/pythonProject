if __name__ == "__main__":
    print(((lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args))))(lambda f: lambda n: 1 if n == 0 else n * f(n-1)))(5))
