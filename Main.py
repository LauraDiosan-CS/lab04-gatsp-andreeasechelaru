from Utils import function
from GA import GA

def read_data():
    """
        Read data from file "in.txt"
    first line: number of cities (n)
    second - n+1 line: matrix of distances between cities
    :return:
    """
    f = open("input/hard.txt", "r")
    n = int(f.readline())
    matrix = []
    for i in range(n):
        row = []
        line = f.readline().split(",")
        for j in range(n):
            row.append(int(line[j]))
        matrix.append(row)
    return [n, matrix]


def main():
    n, matrix = read_data()
    # initialise de GA parameters
    gaParam = {'popSize': 50, 'noGen': 100, 'k': 5}
    # problem parameters
    problParam = {'matrix': matrix, 'noNodes': n, 'function': function}

    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()

    for g in range(gaParam['noGen']):
        # logic alg
        # ga.oneGenerationElitism()
        ga.oneGenerationSteadyState()
        bestChromo = ga.bestChromosome()
        print('Best solution in generation ' + str(g) + ' is: x = ' + str(bestChromo.repres) + ' f(x) = ' + str(
            bestChromo.fitness))



main()