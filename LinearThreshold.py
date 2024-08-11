import random

count = 0

def make_List(file):
    data = open(file, 'r')

    initialization = data.readline().split()

    nodes = int(initialization[0])
    edges = int(initialization[1])

    length = nodes

    list1 = [[] for i in range(length)]
    list2 = [[] for i in range(length)]

    for i in range(edges):
        edge = data.readline().split()

        start_node = int(edge[0])
        end_node = int(edge[1])

        list1[end_node].append(start_node)

    for i in range(len(list1)):
        neighbors = len(list1[i])

        if neighbors > 0:
            prob = 1/neighbors - 0.01
            randomize = random.random()

            incoming = (int) (randomize // prob)
            if (incoming < neighbors):
                list2[list1[i][incoming]].append(i)

    return list2

def DFS(list, node, visited=None):
    if visited is None:
        visited = []
    visited.append(node)

    global count
    count += 1

    for w in list[node]:
        if w not in visited:
            DFS(list, w, visited)

    return visited


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