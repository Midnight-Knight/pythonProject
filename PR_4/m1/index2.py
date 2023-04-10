class MyClass:
    def my_method(self):
        print("Hello, world!")

if __name__ == "__main__":
    obj = MyClass()
    method_name = "my_method"

    if hasattr(obj, method_name):
        method = getattr(obj, method_name)
        method()
    else:
        print(f"Метод {method_name} не найден")