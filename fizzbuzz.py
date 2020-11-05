# Creating the FizzBuzz class which will be the Parent class to the Fizz and Buzz classes
class FizzBuzz:
    def __init__(self):
        self.fizzbuzz = [3, 5]  # Assigning the fizz and buzz values as an array so we can test fizzbuzz

    def fizzbuzz_checker(self, num):
        # If the number is cleanly divisible by both numbers then we should return FizzBuzz
        if (num % self.fizzbuzz[0] == 0) and (num % self.fizzbuzz[1] == 0):
            return "FizzBuzz"
        else:  # Otherwise return the number
            return num


# test = FizzBuzz()
# print(test.fizzbuzz_checker(30))
