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

        self.basicOperation += 1
        return self.gcd(n, m % n)
    #Recursive Implmentation of Fibanacci
    def fibonacci(self, n):
        if n < 2:
            return n
        else:
            self.basicOperation += 1
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def fibanacciFormula(self, n):

        #used this for sequence instead of iterative algorithm

        oslash = ((1 + math.sqrt(5)) / 2)
        oslashHat = -1 / oslash
        return (1 / math.sqrt(5)) * ((oslash ** n) - (oslashHat ** n - 1))

    def reset(self):
        self.basicOperation = 0

    def expDecByOne(self, a, n):
        # Decrease By one
        if n <= 0:
            return 1
        else:
            self.basicOperation += 1
            return a * self.expDecByOne(a, n - 1)

    def expDecByConstFact(self, a, n):
        if n == 0:
            return 1
        elif (n % 2) == 0:
            self.basicOperation += 1
            return self.expDecByConstFact(a, n/2)**2
        else:
            self.basicOperation += 2
            return a*(self.expDecByConstFact(a, (n-1)/2) **2)

    def devideAndConquer(self, a, n):
        if n == 0:
            return 1
        else:
            if n % 2 == 0:
                self.basicOperation += 1
                return self.devideAndConquer(a, n / 2) * self.devideAndConquer(a, n / 2)
            else:
                self.basicOperation += 2
                return a * self.devideAndConquer(a, (n - 1)/ 2) * self.devideAndConquer(a, (n - 1) / 2)

    def getBasicOp(self):
        return self.basicOperation

    def selectionSort(self, array):
        numOfComparisons = []
        for i in range(0, len(array)-1):
            biggerIndex = 0
            for j in range (1, len(array)-i):
                self.basicOperation += 1
                numOfComparisons.append(self.basicOperation)
                if array[j] >= array[biggerIndex]:
                    biggerIndex = j
            array[biggerIndex], array[j] = array[len(array)-i-1], array[biggerIndex]
        return self.basicOperation


    def insertionSort(self, array):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            self.basicOperation += 2
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return self.basicOperation