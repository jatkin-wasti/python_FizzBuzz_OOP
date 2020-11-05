from fizz import Fizz


class Buzz(Fizz):
    def __init__(self):
        super().__init__()
        self.buzz = 5

    def buzz_checker(self, num):
        if num % self.buzz == 0:
            return "Buzz"
        else:
            return num

    def fizzbuzz_loop(self, num):
        for _ in range(num):
            if self.fizzbuzz_checker(_) == "FizzBuzz":
                print("FizzBuzz")
            elif self.fizz_checker(_) == "Fizz":
                print("Fizz")
            elif self.buzz_checker(_) == "Buzz":
                print("Buzz")
            else:
                print(_)


test = Buzz()
test.fizzbuzz_loop(100)
