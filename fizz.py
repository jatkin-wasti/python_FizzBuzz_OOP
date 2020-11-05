from fizzbuzz import FizzBuzz


class Fizz(FizzBuzz):
    def __init__(self):
        super().__init__()
        self.fizz = 3

    def fizz_checker(self, num):
        if num % self.fizz == 0:
            return "Fizz"
        else:
            return num


# test = Fizz()
# print(test.fizz_checker(15))
