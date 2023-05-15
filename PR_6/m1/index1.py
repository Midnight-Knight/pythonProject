def deriv(f, h=0.0001):
    def f_prime(x):
        return (f(x + h) - f(x - h)) / (2 * h)
    return f_prime

if __name__ == "__main__":
    f = lambda x: x ** 3
    f_prime = deriv(f)
    print(f_prime(5))