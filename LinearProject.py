import numpy as np
from matplotlib import pyplot

if __name__ == '__main__':
    file = 'TextFiles/BFS_DFS.txt'

    data = open(file, 'r')

    initialization = data.readline().split()

    nodes = int(initialization[0])

    for i in range(nodes):
        sum = 0
        for j in range(100):
            list = make_List(file)
            count = 0
            DFS(list, 0)
            sum += count

        print(sum/100)