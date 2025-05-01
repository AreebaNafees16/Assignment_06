class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self  # The object itself is the iterator

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # End of iteration
        value = self.current
        self.current -= 1
        return value

# Example usage in a for-loop
count = Countdown(5)

for num in count:
    print(num)
