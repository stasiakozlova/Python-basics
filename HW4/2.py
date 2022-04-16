class ReverseIter:

    k = 0

    def __init__(self, mylist):
        self.mylist = mylist
        self.length = len(self.mylist)

    def __next__(self):
        self.k += 1
        if self.k <= self.length:
            return self.mylist[-self.k]
        else:
            raise StopIteration
