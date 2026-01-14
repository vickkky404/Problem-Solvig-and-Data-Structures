# 👉 Create a class Car
# 👉 Create two objects of it
# 👉 Print both objects

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"