class OhMyList:
    def __init__(self):
        self.length = 0
        self.capacity = 8
        self.array = (self.capacity * ctypes.py_object)()

    def append(self, item):
        if self.length == self.capacity:
            self._resize(self.capacity*2)
        self.array[self.length] = item
        self.length += 1

    def _resize(self, new_cap):
        new_arr = (new_cap * ctypes.py_object)()
        for idx in range(self.length):
            new_arr[idx] = self.array[idx]
        self.array = new_arr
        self.capacity = new_cap

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        return self.array[idx]


print(OhMyList().append('hello'))