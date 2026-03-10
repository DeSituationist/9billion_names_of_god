class Solution:
    def __init__(self):
        self.res = []
    def fizzBuzz(self, n: int) -> list[str]:
        if n == 0: return self.res[::-1]
        if n % 15 == 0:
            self.res.append('FizzBuzz')
        elif n % 3 == 0:
            self.res.append('Fizz')
        elif n % 5 == 0:
            self.res.append('Buzz')
        else:
            self.res.append(str(n))
        return self.fizzBuzz(n - 1)