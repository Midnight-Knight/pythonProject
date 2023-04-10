import random

class HashTable:
    def __init__(self):
        self.table = []

    def __getitem__(self, key):
        for k, v in self.table:
            if k == key:
                return v
        raise KeyError(key)

    def __setitem__(self, key, value):
        for i, (k, v) in enumerate(self.table):
            if k == key:
                self.table[i] = (key, value)
                break
        else:
            self.table.append((key, value))

    def __delitem__(self, key):
        for i, (k, v) in enumerate(self.table):
            if k == key:
                del self.table[i]
                break
        else:
            raise KeyError(key)

    def __len__(self):
        return len(self.table)

if __name__ == "__main__":
    my_table = HashTable()
    std_table = {}

    for i in range(1000):
        key = random.randint(0, 999)
        value = random.randint(0, 999)
        my_table[key] = value
        std_table[key] = value

    assert len(my_table) == len(std_table)

    for key in std_table:
        assert my_table[key] == std_table[key]

    key = random.randint(0, 999)
    del my_table[key]
    del std_table[key]

    assert len(my_table) == len(std_table)

    for key in std_table:
        assert my_table[key] == std_table[key]
