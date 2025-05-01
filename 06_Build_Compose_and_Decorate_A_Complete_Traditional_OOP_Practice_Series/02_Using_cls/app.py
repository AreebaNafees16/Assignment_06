class Counter:
    count = 0  # Class variable to keep track of object count

    def __init__(self):
        Counter.count += 1  # Increment count when a new object is created

    @classmethod
    def display_count(cls):
        print("Total objects created:", cls.count)


# Example usage
c1 = Counter()
c2 = Counter()
c3 = Counter()

Counter.display_count()
