# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import math

import numpy as np

from asymtoticAnal import algos

numIterations = 0



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
    print(math.floor(fibAlgo.fibanacciFormula(k)))
    print(gcdAlgo.gcd(k+1, k))

    gcd = gcdAlgo.gcd(k+1, k)
    fig0 = plt.figure()
    plt.plot(x, numOfModulos, "bo")
    fig0.suptitle('GCD with worse case input', fontsize=20)
    plt.xlabel('xlabel', fontsize=18)
    plt.ylabel('ylabel', fontsize=16)
    plt.show()


   # print(sequence)
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
def readSmallFile(fileName, array):
    inputsForSorting = []
    f = open("smallSet\\" + fileName, "r")

    for line in f:
        array.append(int(line.strip('\n')))
    return

reversedData = []
numOfComparisonsReversed = []


sortedData = []
numOfComparisonsSorted = []


randomData = []
numOfComparisonsRandom = []

def selectionSortAnalysis_r(start, end, increment):
    x.clear()
    comparisonsSelection = []
    comparisonsInsertion = []
    numComarisonsSelection = []
    numComparisonInsertion = []
    if end > 100:
        for i in range(start, end, increment):
            x.append(i)

            readFile('data' + str(i) + '_rSorted.txt', numComarisonsSelection)
            readFile('data' + str(i) + '_rSorted.txt', numComparisonInsertion)

            comparisonsSelection.append(selectionSortAlgo.selectionSort(numComarisonsSelection))
            comparisonsInsertion.append(insertionSortAlgo.insertionSort(numComparisonInsertion))
            numComarisonsSelection.clear()
            numComparisonInsertion.clear()
    elif end < 100:
        for i in range(start, end, increment):
            x.append(i)

            readSmallFile('data' + str(i) + '_rSorted.txt', numComarisonsSelection)
            readSmallFile('data' + str(i) + '_rSorted.txt', numComparisonInsertion)

            comparisonsSelection.append(selectionSortAlgo.selectionSort(numComarisonsSelection))
            comparisonsInsertion.append(insertionSortAlgo.insertionSort(numComparisonInsertion))
            numComarisonsSelection.clear()
            numComparisonInsertion.clear()


    # print(comparisonsSelection)
    # print(x)
    # print(x)
    # print(numComarisonsSelection)
    # print(numComparisonInsertion)
    fig5 = plt.figure()
    plt.plot(x,comparisonsSelection, "bo")
    plt.plot(x,comparisonsInsertion, "ro")
    plt.title("Selection Sort Reversed Input")
    fig5.suptitle('Reversed', fontsize=20)
    plt.xlabel('xlabel', fontsize=18)
    plt.ylabel('ylabel', fontsize=16)
    plt.show()


def selectionSortAnalysis_sorted(start, end, increment):
    x.clear()
    comparisonsSelection = []
    comparisonsInsertion = []
    numComarisonsSelection = []
    numComparisonInsertion = []

    if end > 100:
        for i in range(start, end, increment):
            x.append(i)
            readFile('data' + str(i) + '_sorted.txt', numComarisonsSelection)
            readFile('data' + str(i) + '_sorted.txt', numComparisonInsertion)

            comparisonsSelection.append(selectionSortAlgo.selectionSort(numComarisonsSelection))
            comparisonsInsertion.append(insertionSortAlgo.insertionSort(numComparisonInsertion))
            numComarisonsSelection.clear()
            numComparisonInsertion.clear()
    elif end < 100:
        for i in range(start, end, increment):
            x.append(i)
            readSmallFile('data' + str(i) + '_sorted.txt', numComarisonsSelection)
            readSmallFile('data' + str(i) + '_sorted.txt', numComparisonInsertion)

            comparisonsSelection.append(selectionSortAlgo.selectionSort(numComarisonsSelection))
            comparisonsInsertion.append(insertionSortAlgo.insertionSort(numComparisonInsertion))
            numComarisonsSelection.clear()
            numComparisonInsertion.clear()

    print(comparisonsSelection)
    print(comparisonsInsertion)
    print(x)
    fig6 = plt.figure()

    plt.plot(x, comparisonsSelection, "bo")
    plt.plot(x, comparisonsInsertion, "ro")
    plt.title("Selection Sort Sorted Input")
    fig6.suptitle('Sorted', fontsize=20)
    plt.xlabel('xlabel', fontsize=18)
    plt.ylabel('ylabel', fontsize=16)
    plt.show()



def selectionSortAnalysis_random(start, end, increment):
    x.clear()
    comparisonsSelection = []
    comparisonsInsertion = []
    numComarisonsSelection = []
    numComparisonInsertion = []


    if end > 100:
        for i in range(start, end, increment):
            x.append(i)
            readFile('data' + str(i) + '.txt', numComarisonsSelection)
            readFile('data' + str(i) + '.txt', numComparisonInsertion)

            comparisonsSelection.append(selectionSortAlgo.selectionSort(numComarisonsSelection))
            comparisonsInsertion.append(insertionSortAlgo.insertionSort(numComparisonInsertion))
            numComarisonsSelection.clear()
            numComparisonInsertion.clear()
    elif end < 100:
        for i in range(start, end, increment):
            x.append(i)
            readSmallFile('data' + str(i) + '.txt', numComarisonsSelection)
            readSmallFile('data' + str(i) + '.txt', numComparisonInsertion)

            comparisonsSelection.append(selectionSortAlgo.selectionSort(numComarisonsSelection))
            comparisonsInsertion.append(insertionSortAlgo.insertionSort(numComparisonInsertion))
            numComarisonsSelection.clear()
            numComparisonInsertion.clear()

    fig7 = plt.figure()
    plt.plot(x, comparisonsSelection, "bo")
    plt.plot(x, comparisonsInsertion, "ro")

    plt.title("Selection Sort with Random Input")
    fig7.suptitle('Random', fontsize=20)
    plt.xlabel('xlabel', fontsize=18)
    plt.ylabel('ylabel', fontsize=16)
    plt.show()

def main():

    mode = input("Select 1, To Enter User Testing Mode: \n"
                 "Select 2, To Enter Scatter Plot Mode:  \n"
                 )

    if mode == '1':
        k = int(input("Ener a valuie for k, to see Fib(k) and GCD(m,n): "))
        fibAlgo.reset();
        print(math.floor(fibAlgo.fibanacciFormula(k)))
        sequence.clear()
        fillFibSequence(k)
        print(sequence)



        a = int(input("please enter a value for a: "))
        n = int(input("please enter a value for n: "))

        algo1 = expAlgo.expDecByOne(a, n)

        algo2 = expAlgo.expDecByConstFact(a, n)

        algo3 = expAlgo.devideAndConquer(a, n)


        print("Computer Using Decrease by 1")
        print(algo1)
        print("Computer Using Decrease by Constant:")

        print((algo2))

        print("Computer Using Decrease and Conquer: ")
        print(algo3)



        selection = []
        insertion = []
        file = []

        listSize = int(input("Please enter a list size n, between 10-100 at an increment of 10: "))

        readSmallFile('data' + str(listSize) + '.txt', file)

        selectionSort = readSmallFile('data' + str(listSize) + '.txt', selection)

        insertionSort = readSmallFile('data' + str(listSize) + '.txt', insertion)

        # selectionSortAlgo.selectionSort(selection)
        print("For selection sort")
        print(selection)
        # insertionSortAlgo.insertionSort(insertion)
        print("For insertion sort")
        print(insertion)
        # selectionSortAnalysis_r(10, listSize, 10)
        # selectionSortAnalysis_random(10, listSize, 10)
        # selectionSortAnalysis_sorted(10, listSize, 10)
        main()

    else:

        basicOperationExponent(400)
        showExp()
        selectionSortAnalysis_r(100, 2000, 300)
        selectionSortAnalysis_random(100, 2000, 300)
        selectionSortAnalysis_sorted(100, 2000, 300)
        kforTaskOne = displayKfor_GCD_FIB(12)
        displayK_for_fib(12)
        print(math.floor(kforTaskOne[0]), kforTaskOne[1])


main()
