import random

count = 0
visited = []

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

def DFS(list, node):
    if node not in visited:
        visited.append(node)
        global count
        count += 1

    for w in list[node]:
        if w not in visited:
            DFS(list, w)

    return visited


if __name__ == '__main__':
    file = 'TextFiles/BFS_DFS.txt'
    groups = 'TextFiles/Starting Nodes'

    data = open(file, 'r')

    initialization = data.readline().split()

    nodes = int(initialization[0])

    numofgroups = int(initialization[0])

    x = []
    ans = [[] for i in range(3)]

    for i in range(numofgroups):
        subgroup = data.readline().split()
        group = int(subgroup[0])
        length = int(subgroup[1])
        x.append(length)
        for j in range(group):
            sum = 0
            next_group = data.readline().split()
            for k in range(100):
                list = make_List(file)
                count = 0
                visited = []
                for node in next_group:
                    DFS(list, int(node))
                sum += count