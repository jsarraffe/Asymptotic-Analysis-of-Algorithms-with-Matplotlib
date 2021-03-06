# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import math



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
    for i in range(0, n):
        sequence.append([math.floor(fibAlgo.fibanacciFormula(i + 1)), math.floor(fibAlgo.fibanacciFormula(i))])



def fillGCD():
    fibAlgo.reset()
    numOfModulos.clear();
    e = 0
    for i in sequence:
        fibAlgo.gcd(i[0], i[1])
        x.append(e+1)  # which one do I use "Plug in n"
        e+=1
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

    w = []
    x.clear()
    for i in range(0,len(sequence)):
        gcdAlgo.reset()
        gcdAlgo.gcd(sequence[i][0],sequence[i][1])
        w.append(gcdAlgo.basicOperation)
        x.append(sequence[i][1])

    superscript = str.maketrans("2", "2")


    fig0 = plt.figure()
    plt.plot(x, numOfModulos, "bo")
    fig0.suptitle(" Euclid's algorithm with consecutive elements of the Fibnacci sequence as inputs", fontsize=12)
    plt.xlabel('k', fontsize=18)
    plt.ylabel('# of divisions', fontsize=16)
    plt.legend([" D(k) ∈ ϴ(log(k))"])

    plt.show()


   # print(sequence)

def displayK_for_fib(k):
    superscript = str.maketrans("2", "²")
    x.clear()
    basicOperations.clear()
    basicOpOfRecursiveAlgo(k)
    fig = plt.figure()
    plt.plot(x, basicOperations, "bo")
    fig.suptitle('Recursive Fibonacci Implementation', fontsize=15)
    plt.xlabel('k', fontsize=18)
    plt.ylabel('# of additions', fontsize=16)
    plt.legend(["A(k) ∈ ϴ(" + "k" + "2".translate(superscript) + ")"])

    plt.show()

def showExp():
    superscript = str.maketrans("n", "ⁿ")
    fig3 = plt.figure()
    plt.plot(x, decByConst, "bo")
    plt.plot(x, decByOneOperations, "go")
    plt.plot(x, devAndConquer, "ro")
    fig3.suptitle('Comparison of algorithms for exponentiation', fontsize=16)
    plt.xlabel(" n ")
    plt.ylabel('# of multiplications', fontsize=18)
    plt.legend(["Decrease-by-constant: M(n) ∈ ϴ(log(n))", "Decrease-by-one: M(n) ∈   ϴ(n)", "Divide-and-conquer: M(n) ∈  ϴ(n)"])

    plt.show()
    figx = plt.figure()
    plt.plot(x, decByConst, "bo")
    figx.suptitle('Decrease-By-Constant closer look', fontsize=16)
    plt.xlabel(" n ")
    plt.ylabel('# of multiplications', fontsize=18)
    plt.legend(["Decease-by-Constant: M(n) ∈ ϴ(log(n))"])

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
    superscript = str.maketrans("2", "²")


    fig5 = plt.figure()
    plt.plot(x,comparisonsSelection, "bo")
    plt.plot(x,comparisonsInsertion, "ro")
    fig5.suptitle('Reversed input for Sorting Algorithms', fontsize=15)
    plt.xlabel('n', fontsize=18)
    plt.ylabel('# of comparisons', fontsize=16)
    plt.legend(["Selection Sort: C(n) ∈ ϴ(" + "n" + "2".translate(superscript) + ")", "Insertion Sort: C(n) ∈ ϴ(" + "n" + "2".translate(superscript) + ")"])

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

    # print(comparisonsSelection)
    # print(comparisonsInsertion)
    # print(x)
    fig6 = plt.figure()

    superscript = str.maketrans("2", "²")

    plt.plot(x, comparisonsSelection, "bo")
    plt.plot(x, comparisonsInsertion, "ro")
    fig6.suptitle('Sorted input for Sorting Algorithms', fontsize=15)
    plt.xlabel('size of list as n', fontsize=18)
    plt.ylabel('# of comparisons', fontsize=16)

    plt.legend(["Selection Sort: C(n) ∈ ϴ(" + "n" + "2".translate(superscript) + ")", "Insertion Sort: C(n) ∈ ϴ (" + "n)"])
    plt.show()

    figI = plt.figure()
    plt.plot(x, comparisonsInsertion, "ro")
    figI.suptitle('A closer look at Insertion with Sorted Input', fontsize=15)
    plt.xlabel('size of list as n', fontsize=18)
    plt.ylabel('# of comparisons', fontsize=16)

    plt.legend(
        ["Selection Sort: C(n) ∈ ϴ(" + "n" + "2".translate(superscript) + ")", "Insertion Sort: C(n) ∈ ϴ (" + "n)"])
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
    superscript = str.maketrans("2", "²")
    plt.plot(x, comparisonsSelection, "bo")
    plt.plot(x, comparisonsInsertion, "ro")

    fig7.suptitle('Random input for Sorting Algorithms', fontsize=15)
    plt.xlabel('size of list as n', fontsize=18)
    plt.ylabel('# of comparisons', fontsize=16)
    plt.legend(["Selection Sort: C(n) ∈ ϴ(" + "n" + "2".translate(superscript) + ")", "Insertion Sort: C(n) ∈ ϴ (" + "n" + "2".translate(superscript) + ")"])

    plt.show()

def main():


    mode = input("Select 1 To Enter User Testing Model: \n"
                 "Select 2 To Enter Scatter Plot Model:  \n"
                 "Select q To Quit:  \n"
                 )

    if mode == '1':
        k = int(input("Ener a value for k, to see Fib(k) and GCD(k+1,k) =  "))
        fibAlgo.reset();
        print("Fib(k) =  " + str(math.floor((fibAlgo.fibanacciFormula(k)))))

        sequence.clear()
        fillFibSequence(k)
        gcdAlgo.reset()
        x = gcdAlgo.gcd(sequence[len(sequence) - 1][0], sequence[len(sequence) - 1][1])

        print("GCD(k+1,k) =  " + str(x))

        print(sequence)

        a = int(input("please enter a value for a: "))
        n = int(input("please enter a value for n: "))

        algo1 = expAlgo.expDecByOne(a, n)

        algo2 = expAlgo.expDecByConstFact(a, n)

        algo3 = expAlgo.devideAndConquer(a, n)

        print("Computed Using Decrease-by-1")
        print(algo1)
        print("Computed Using Decrease-by-Constant:")

        print((algo2))

        print("Computed Using Decrease-and-Conquer: ")
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
        print("\n")
    elif mode == '2':
        decByConst.clear()
        devAndConquer.clear()
        decByOneOperations.clear()
        basicOperationExponent(400)
        showExp()
        selectionSortAnalysis_r(100, 4000, 500)
        selectionSortAnalysis_random(100, 4000, 500)
        selectionSortAnalysis_sorted(100, 4000, 500)
        displayKfor_GCD_FIB(30)
        displayK_for_fib(20)
        # print(math.floor(kforTaskOne[0]), kforTaskOne[1])
        main()
        print("\n")




main()
