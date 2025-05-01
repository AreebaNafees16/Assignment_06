class Engine:
    def start(self):
        print("Engine started.")


class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Engine is a part of Car

    def start_car(self):
        print("Starting the car...")
        self.engine.start()  # Accessing Engine's method through Car


# Example usage
engine_obj = Engine()
car_obj = Car(engine_obj)

car_obj.start_car()
