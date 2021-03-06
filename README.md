# Task
## FizzBuzz with Classes
### Part 1
- Write program that prints numbers 1-100
- For multiples of 3, print the word "Fizz" instead
- For multiples of 5, print the word "Buzz" instead
- For multiples of both 3 and 5, print the word "FizzBuzz" instead
### Part 2
- Allow for users to input which numbers to substitute for "Fizz" and "Buzz"
## Solution
### FizzBuzz class
- This class is the parent class which defaults the fizz and buzz values to 3 and 5 respectively
- It has a fizzbuzz_checker method that takes a number and checks if it meets the FizzBuzz conditions 
(i.e. is it a multiple of both of them)
- Depending on the result, it either returns the "FizzBuzz" string or the passed number
```
class FizzBuzz:
    def __init__(self):
        self.fizzbuzz = [3, 5]  # Assigning the fizz and buzz values as an array so we can test fizzbuzz

    def fizzbuzz_checker(self, num):
        # If the number is cleanly divisible by both numbers then we should return FizzBuzz
        if (num % self.fizzbuzz[0] == 0) and (num % self.fizzbuzz[1] == 0):
            return "FizzBuzz"
        else:  # Otherwise return the number
            return num
```
### Fizz class
- This class is the child class to the FizzBuzz class
- It inherits all functionality from the FizzBuzz class but also defines the Fizz number
- It has a fizz_checker method that checks if the passed number is a multiple of the Fizz number
- Depending on the result it either returns the "Fizz" string or the passed number 
```
from fizzbuzz import FizzBuzz  # Importing the FizzBuzz class so that we can inherit from it


class Fizz(FizzBuzz):
    def __init__(self, fizznum):
        super().__init__()  # Calling the super classes initialisation method
        self.fizz = fizznum  # And assigning our fizz value

    def fizz_checker(self, num):  # Checking if the number is a multiple of 3
        if num % self.fizz == 0:
            return "Fizz"  # If so we return Fizz
        else:
            return num  # If not we return the number
```
### Buzz class
- This class is the child class to the Fizz class
- It inherits all functionality from the Fizz class (including functionality from the FizzBuzz class) but also defines 
the Buzz number
- It has a buzz_checker method that checks if the passed number is a multiple of the Buzz number
- Depending on the result it either returns the "Buzz" string or the passed number
- It also has the fizzbuzz_loop method which loops through numbers from 1 to the provided value
- For each number it uses the inherited fizzbuzz_checker and fizz_checker methods along with its own buzz_checker
 to determine if it meets any of the criteria
- If it meets any of the criteria, it prints the relevant string. If not, it prints the number                                                                                                              
```
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
```
### Testing code
```
test = Buzz(10, 4)  # Creating an instance of the Buzz class
test.fizzbuzz_loop(100)  # Calling the fizzbuzz_loop function
```