class Collector:
    instances = []

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        instance = self.cls(*args, **kwargs)
        Collector.instances.append(instance)
        return instance

    def get_objects(self):
        return Collector.instances

def collect(cls):
    return Collector(cls)

if __name__ == "__main__":
    @collect
    class MyClass:
        pass


    a = MyClass()
    b = MyClass()
    c = MyClass()

    print(MyClass.get_objects())