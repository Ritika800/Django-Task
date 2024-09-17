class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        # Create an iterator state
        self._iter_state = 0

    def __iter__(self):
        # Reset iterator state when a new iterator is created
        self._iter_state = 0
        return self

    def __next__(self):
        if self._iter_state == 0:
            self._iter_state = 1
            return {'length': self.length}
        elif self._iter_state == 1:
            self._iter_state = 2
            return {'width': self.width}
        else:
            # Stop iteration
            raise StopIteration

# Example usage:
rect = Rectangle(10, 5)
for item in rect:
    print(item)
