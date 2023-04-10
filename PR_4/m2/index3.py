class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

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
        return sum(len(slot) for slot in self.table)

    def __iter__(self):
        self.current_index = 0
        self.current_slot = 0
        return self

    def __next__(self):
        while self.current_slot < len(self.table[self.current_index]):
            item = self.table[self.current_index][self.current_slot]
            self.current_slot += 1
            return item[0]
        self.current_index += 1
        self.current_slot = 0
        while self.current_index < len(self.table):
            if self.table[self.current_index]:
                item = self.table[self.current_index][self.current_slot]
                self.current_slot += 1
                return item[0]
            self.current_index += 1
            self.current_slot = 0
        raise StopIteration

if __name__ == "__main__":
    my_dict = HashTable()
    my_dict["apple"] = 1
    my_dict["banana"] = 2
    my_dict["cherry"] = 3

    for key in my_dict:
        print(key)
