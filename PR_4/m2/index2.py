class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def __setitem__(self, key, value):
        index = hash(key) % self.size
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def __getitem__(self, key):
        index = hash(key) % self.size
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)

    def __delitem__(self, key):
        index = hash(key) % self.size
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return
        raise KeyError(key)

    def __len__(self):
        return sum(len(bucket) for bucket in self.table)

    def __contains__(self, key):
        index = hash(key) % self.size
        for item in self.table[index]:
            if item[0] == key:
                return True
        return False

    def clear(self):
        self.table = [[] for _ in range(self.size)]

    def items(self):
        return [(key, value) for bucket in self.table for key, value in bucket]

if __name__ == "__main__":
    # Создание хэш-таблицы
    ht = HashTable()

    # Добавление элементов
    ht['one'] = 1
    ht['two'] = 2
    ht['three'] = 3

    # Получение элементов
    print(ht['one'])  # 1
    print(ht['two'])  # 2
    print(ht['three'])  # 3

    # Изменение элемента
    ht['one'] = 100
    print(ht['one'])  # 100

    # Удаление элемента
    del ht['three']
    try:
        print(ht['three'])
    except KeyError:
        print('KeyError')

    # Проверка наличия элемента
    print('one' in ht)  # True
    print('four' in ht)  # False

    # Очистка хэш-таблицы
    ht.clear()
    print(len(ht))  # 0

    # Получение всех элементов
    ht['one'] = 1
    ht['two'] = 2
    ht['three'] = 3
    print(ht.items())  # [('two', 2), ('three', 3), ('one', 1)]
