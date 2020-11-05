from fizzbuzz import FizzBuzz  # Importing the FizzBuzz class so that we can inherit from it


class Fizz(FizzBuzz):
    def __init__(self):
        super().__init__()  # Calling the super classes initialisation method
        self.fizz = 3  # And assigning our fizz value

    def fizz_checker(self, num):  # Checking if the number is a multiple of 3
        if num % self.fizz == 0:
            return "Fizz"  # If so we return Fizz
        else:
            return num  # If not we return the number


# test = Fizz()
# print(test.fizz_checker(15))
