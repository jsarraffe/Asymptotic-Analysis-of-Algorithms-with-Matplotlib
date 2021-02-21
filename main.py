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
insertionSortAlgo = algos()

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


    print(sequence)
    return (fib, gcd)
def displayK_for_fib(k):
    x.clear()
    basicOperations.clear()
    basicOpOfRecursiveAlgo(k)
    fig = plt.figure()
    plt.plot(x, basicOperations, "bo")
    fig.suptitle('Kth term for fibnacci sequence', fontsize=20)
    plt.xlabel('xlabel', fontsize=18)
    plt.ylabel('ylabel', fontsize=16)
    plt.show()

def showExp():
    fig3 = plt.figure()
    plt.plot(x, decByConst, "bo")
    plt.plot(x, decByOneOperations, "go")
    plt.plot(x, devAndConquer, "ro")
    fig3.suptitle('Exponentiation', fontsize=20)
    plt.xlabel('xlabel', fontsize=18)
    plt.ylabel('ylabel', fontsize=16)
    plt.legend(["Dec by Const", "Dec by one", "devid and conquer"])

    plt.show()

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
    numComarisonsReversed = []
    for i in range(100, 2000, 400):
        x.append(i)
        readFile('data' + str(i) + '_rSorted.txt', reversedData)


        numComarisonsReversed.append( selectionSortAlgo.selectionSort(reversedData))

        numOfComparisonsReversed.append(selectionSortAlgo.insertionSort(reversedData))

    fig5 = plt.figure()
    print(x)
    print(numComarisonsReversed)
    print(numOfComparisonsReversed)
    plt.plot(x, numOfComparisonsReversed, "bo")
    plt.plot(x, numComarisonsReversed, "ro")
    plt.title("Selection Sort Reversed Input")
    fig5.suptitle('Reversed', fontsize=20)
    plt.xlabel('xlabel', fontsize=18)
    plt.ylabel('ylabel', fontsize=16)

    plt.legend(["selection sort"," insertion sort"])
    plt.show()


def selectionSortAnalysis_sorted():
    x.clear()
    numComparisonsInsertion = []
    for i in range(100, 2000, 400):
        x.append(i)
        readFile('data' + str(i) + '_sorted.txt', sortedData)


        numOfComparisonsSorted.append(selectionSortAlgo.selectionSort(sortedData))

        numComparisonsInsertion.append(insertionSortAlgo.insertionSort(sortedData))
    fig6 = plt.figure()
    plt.plot(x, numOfComparisonsSorted, "bo")
    plt.plot(x, numComparisonsInsertion, "ro")
    plt.title("Selection Sort Sorted Input")
    fig6.suptitle('Sorted', fontsize=20)
    plt.xlabel('xlabel', fontsize=18)
    plt.ylabel('ylabel', fontsize=16)
    plt.legend(["selection sort"," insertion sort"])

    plt.show()



def selectionSortAnalysis_random():
    x.clear()
    numComparisonsInsertion = []
    for i in range(100, 2000, 400):
        x.append(i)
        readFile('data' + str(i) + '.txt', randomData)


        numOfComparisonsRandom.append(selectionSortAlgo.selectionSort(randomData))
        numComparisonsInsertion.append(insertionSortAlgo.selectionSort(randomData))
    fig7 = plt.figure()
    plt.plot(x, numOfComparisonsRandom, "bo")
    plt.plot(x, numComparisonsInsertion, "ro")
    plt.title("Selection Sort with Random Input")
    fig7.suptitle('Random', fontsize=20)
    plt.xlabel('xlabel', fontsize=18)
    plt.ylabel('ylabel', fontsize=16)
    plt.legend(["selection sort"," insertion sort"])
    plt.show()

def main():

    basicOperationExponent(400)
    showExp()
    selectionSortAnalysis_r()
    selectionSortAnalysis_random()
    selectionSortAnalysis_sorted()
    kforTaskOne = displayKfor_GCD_FIB(12)
    displayK_for_fib(12)
    print(math.floor(kforTaskOne[0]), kforTaskOne[1])


    insertionSort = []
    readFile('data100.txt', insertionSort)
    insertionSortAlgo.insertionSort(insertionSort)
    print(insertionSort)

main()
'''
input_list = [[2, 1],[3, 2], [5, 3], [8, 5], [13, 8], [21, 13], [34, 21], [55, 34], [89,55],[144, 89],[233, 144],[377, 233], [610, 377], [987, 610],[1597, 987], [2854, 1597], [4181, 2584], [6765, 4181], [10946    , 6765], [17711, 10946], [28657, 17711], [46368, 28657], [75025, 46368], [121393, 75025], [196418, 121393],     [317811, 196418]]
'''