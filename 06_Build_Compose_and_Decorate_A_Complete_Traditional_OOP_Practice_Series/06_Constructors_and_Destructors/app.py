class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")


# Example usage
log = Logger()

# Optionally delete the object to trigger the destructor
del log
