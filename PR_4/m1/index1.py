class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == "__main__":
    obj = MyClass(1, 2)
    obj_fields = [field for field in vars(obj) if not field.startswith("__")]
    print(obj_fields)
