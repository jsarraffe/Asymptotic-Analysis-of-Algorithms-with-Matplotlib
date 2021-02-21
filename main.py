# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import math

import numpy as np

from asymtoticAnal import algos



fibAlgo = algos()
expAlgo = algos()
gcdAlgo = algos()
selectionSortAlgo = algos()

basicOperations = []
decByOneOperations = []
decByConst = []
devAndConquer = []
sequence = []
numOfModulos = []

x = []

def basicOpOfRecursiveAlgo(kforFib):
    x.clear()
    for i in range(1, kforFib):
        x.append(i)
        fibAlgo.fibonacci(i)
        basicOperations.append(fibAlgo.getBasicOp())
        fibAlgo.reset()

def fillFibSequence(n):
    for i in range(1, n):
        sequence.append([math.floor(fibAlgo.fibanacciFormula(i + 2)), math.floor(fibAlgo.fibanacciFormula(i + 1))])


def fillGCD():
    fibAlgo.reset()
    for i in sequence:
        fibAlgo.gcd(i[0], i[1])
        x.append(i[1])  # which one do I use "Plug in n"
        numOfModulos.append(fibAlgo.getBasicOp())
        fibAlgo.reset()

def basicOperationExponent(n):
    expAlgo.reset()
    basicOperations.clear()
    x.clear()
    for i in range(1, n,10):
        x.append(i)
        expAlgo.expDecByOne(2,i)
        decByOneOperations.append(expAlgo.basicOperation)
        expAlgo.reset()

        expAlgo.expDecByConstFact(2,i)
        decByConst.append(expAlgo.basicOperation)
        expAlgo.reset()

        expAlgo.devideAndConquer(2,i)
        devAndConquer.append(expAlgo.basicOperation)
        expAlgo.reset()

def displayKfor_GCD_FIB(k):

    x.clear()
    fibAlgo.reset()
    sequence.clear()
    numOfModulos.clear()
    fillFibSequence(k)
    fillGCD()

    fib = fibAlgo.fibanacciFormula(k)
    gcd = gcdAlgo.gcd(k+1, k)
    fig0 = plt.figure()
    plt.plot(x, numOfModulos, "bo")
    fig0.suptitle('GCD with worse case input', fontsize=20)
    plt.xlabel('xlabel', fontsize=18)
    plt.ylabel('ylabel', fontsize=16)
    plt.show()
    plt.show()

    # basicOpOfRecursiveAlgo(6)
    # figRecursiveFib = plt.figure()
    # figRecursiveFib.suptitle('K for Recursive Fibanacci', fontsize=20)
    # plt.plot(x, basicOperations, "bo")

    print(sequence)
    return (fib, gcd)

def showExp1():
    fig = plt.figure()
    plt.plot(x, decByOneOperations, "bo")
    fig.suptitle('Dec By one', fontsize=20)
    plt.xlabel('xlabel', fontsize=18)
    plt.ylabel('ylabel', fontsize=16)
    plt.show()

def showExp2():
    fig2 = plt.figure()
    plt.plot(x, decByConst, "bo")
    plt.title("Decrease by Const")
    fig2.suptitle('Dec By const', fontsize=20)
    plt.xlabel('xlabel', fontsize=18)
    plt.ylabel('ylabel', fontsize=16)
    plt.show()
def showExp3():
    fig3 = plt.figure()
    plt.plot(x, devAndConquer, "bo")
    plt.title("Divide and Conquer")
    plt.xlabel('xlabel', fontsize=18)
    plt.ylabel('ylabel', fontsize=16)
    plt.show()



basicOperationExponent(400)
showExp1()
showExp2()
showExp3()
kforTaskOne = displayKfor_GCD_FIB(39)
print(math.floor(kforTaskOne[0]), kforTaskOne[1])


def readFile(fileName, array):
    inputsForSorting = []
    f = open("testSet\\" + fileName,"r")
    for line in f:
        array.append(int(line.strip('\n')))
    return









reversedData = []
numOfComparisonsReversed = []

sortedData = []
numOfComparisonsSorted = []

randomData = []
numOfComparisonsRandom = []

def selectionSortAnalysis_r():
    x.clear()
    for i in range(100, 1000, 100):
        x.append(i)
        readFile('data' + str(i) + '_rSorted.txt', reversedData)

        reversed = selectionSortAlgo.selectionSort(reversedData)
        numOfComparisonsReversed.append(reversed)
    fig5 = plt.figure()
    plt.plot(x, numOfComparisonsReversed, "bo")
    plt.title("Selection Sort Reversed Input")
    fig5.suptitle('Reversed', fontsize=20)
    plt.xlabel('xlabel', fontsize=18)
    plt.ylabel('ylabel', fontsize=16)
    plt.show()
def selectionSortAnalysis_sorted():
    x.clear()
    for i in range(100, 1000, 100):
        x.append(i)
        readFile('data' + str(i) + '_sorted.txt', sortedData)

        sorted = selectionSortAlgo.selectionSort(sortedData)
        numOfComparisonsSorted.append(sorted)
    fig6 = plt.figure()
    plt.plot(x, numOfComparisonsSorted, "bo")
    plt.title("Selection Sort Sorted Input")
    fig6.suptitle('Sorted', fontsize=20)
    plt.xlabel('xlabel', fontsize=18)
    plt.ylabel('ylabel', fontsize=16)
    plt.show()
def selectionSortAnalysis_random():
    x.clear()
    for i in range(100, 1000, 100):
        x.append(i)
        readFile('data' + str(i) + '.txt', randomData)

        randData = selectionSortAlgo.selectionSort(randomData)
        numOfComparisonsRandom.append(randData)
    fig7 = plt.figure()
    plt.plot(x, numOfComparisonsRandom, "bo")
    plt.title("Selection Sort with Random Input")
    fig7.suptitle('Random', fontsize=20)
    plt.xlabel('xlabel', fontsize=18)
    plt.ylabel('ylabel', fontsize=16)
    plt.show()
selectionSortAnalysis_r()
selectionSortAnalysis_random()
selectionSortAnalysis_sorted()




'''
input_list = [[2, 1],[3, 2], [5, 3], [8, 5], [13, 8], [21, 13], [34, 21], [55, 34], [89,55],[144, 89],[233, 144],[377, 233], [610, 377], [987, 610],[1597, 987], [2854, 1597], [4181, 2584], [6765, 4181], [10946    , 6765], [17711, 10946], [28657, 17711], [46368, 28657], [75025, 46368], [121393, 75025], [196418, 121393],     [317811, 196418]]
'''