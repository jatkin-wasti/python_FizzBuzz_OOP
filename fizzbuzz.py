class FizzBuzz:
    def __init__(self):
        self.fizzbuzz = [3, 5]

    def fizzbuzz_checker(self, num):
        if (num % self.fizzbuzz[0] == 0) and (num % self.fizzbuzz[1] == 0):
            return "FizzBuzz"
        else:
            return num


# test = FizzBuzz()
# print(test.fizzbuzz_checker(30))
