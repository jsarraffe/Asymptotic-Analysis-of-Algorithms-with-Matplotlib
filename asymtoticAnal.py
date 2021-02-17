import matplotlib.pyplot as plt
import math


class algos:
    def __init__(self):
        self.basicOperation = 0
        self.sequence = []

    # Rule of them when calling a function in a CLASS PUT SELF
    def gcd(self, m, n):
        if m == 0:
            return n
        if n == 0:
            return m
        return self.gcd(n, m % n)

    def fibonacci(self, n):
        if n < 2:
            return n
        else:
            self.basicOperation += 1
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def fibanacciFormula(self, n):

        oslash = ((1 + math.sqrt(5)) / 2)
        oslashHat = -1 / oslash
        return ((1 / math.sqrt(5)) * ((oslash ** n) - (oslashHat ** n - 1)))

    def reset(self):
        self.basicOperation = 0

    def getBasicOp(self):
        return self.basicOperation
