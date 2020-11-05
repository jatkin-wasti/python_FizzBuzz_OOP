from fizz import Fizz  # Importing the Fizz class so that we can inherit from it


class Buzz(Fizz):
    def __init__(self, buzznum, fizznum):
        super().__init__(fizznum)  # Calling the initialisation method from the Fizz class
        self.buzz = buzznum  # Assigning our Buzz value
        self.fizzbuzz = [fizznum, buzznum]

    def buzz_checker(self, num):  # Checking if the number is a multiple of 5
        if num % self.buzz == 0:
            return "Buzz"  # If so return Buzz
        else:
            return num  # If not return the number

    def fizzbuzz_loop(self, num):  # Looping from 1 to the provided number
        for _ in range(num):
            if self.fizzbuzz_checker(_) == "FizzBuzz":  # First we check if it should be FizzBuzz
                print("FizzBuzz")
            elif self.fizz_checker(_) == "Fizz":  # If not we check if it should be Fizz
                print("Fizz")
            elif self.buzz_checker(_) == "Buzz":  # If not we check if it should be Buzz
                print("Buzz")
            else:  # If not then we simply return the value
                print(_)


test = Buzz(10, 4)  # Creating an instance of the Buzz class
test.fizzbuzz_loop(100)  # Calling the fizzbuzz_loop function
