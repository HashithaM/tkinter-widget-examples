def add(*args):
    sum = 0
    print(args[2])
    for number in args:
        sum += number
    return sum


# Here the args is a tuple remember to note about tuples
sums = add(1, 2, 3, 4, 5)
print(sums)


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)


# Here kwargs is a dictionary
calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan")
print(my_car.make)
# When using get method all the arguments have not to be provided


