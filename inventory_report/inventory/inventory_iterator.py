from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, lista):
        self.lista = lista
        self.limit = 0

    def __next__(self):
        limit = self.limit
        if limit == self.lista:
            raise StopIteration
        else:
            item = self.lista[self.limit]
            self.limit = limit + 1
            return item
