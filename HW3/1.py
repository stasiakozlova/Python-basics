class OneIndexedList:
    """Класс имитирует поведение списка, использующего индексацию, начинающуюся с 1"""

    def __init__(self, items=None):
        self.items = items or []

    def __setitem__(self, index, element):
        self.items[index-1] = element

    def __getitem__(self, index):
        return self.items[index-1]


array = OneIndexedList([56, 76, 74])
array[1] = 3
print(array[1])
