import random

if __name__ == '__main__':
    file = 'TextFiles/p2p-Gnutella08.txt'

    data = open(file, 'r')

    initialization = data.readline().split()

    nodes = int(initialization[0])
    edges = int(initialization[1])

    size = 3
    list = random.sample(range(nodes), size)

    print(list)