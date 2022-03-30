class OneIndexedList:
    """Класс имитирует поведение списка, использующего индексацию, начинающуюся с 1"""

    def __init__(self, items=None):
        self.items = items or []

    def __setitem__(self, element):
        self.items.append(element)
        
    def __getitem__(self, index):
        return self.items[index-1]
