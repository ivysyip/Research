import random
import math

count = 0

def make_List(file):
    data = open(file, 'r')

    initialization = data.readline().split()

    nodes = int(initialization[0])
    edges = int(initialization[1])

    length = nodes

    list = [[] for i in range(length)]

    for i in range(edges):
        edge = data.readline().split()

        start_node = int(edge[0])
        end_node = int(edge[1])

        randomize = random.random()

        if randomize <= 0.7:
            list[start_node].append(end_node)

    return list


def DFS(list, node, visited=None):
    if visited is None:
        visited = []

    global count

    if node not in visited:
        visited.append(node)
        count += 1

    for w in list[node]:
        if w not in visited:
            DFS(list, w, visited)

    return visited


if __name__ == '__main__':
    file = 'TextFiles/p2p-Gnutella08.txt'

    data = open(file, 'r')

    initialization = data.readline().split()

    nodes = int(initialization[0])

    max_visited = []
    maximize = []

    list = make_List(file)

    for j in range(1):
        curr_max_visited = []
        curr_max_count = -math.inf
        curr_max_node = 0

        for i in range(nodes):
            if i not in maximize:
                count = 0

                if j == 0:
                    n_visited = DFS(list, i)
                else:
                    n_visited = DFS(list, i, max_visited)

                if count > curr_max_count:
                    curr_max_count = count
                    curr_max_visited = n_visited
                    curr_max_node = i


        for n in curr_max_visited:
            if n not in max_visited:
                max_visited.append(n)

        maximize.append(curr_max_node)

        print(maximize)