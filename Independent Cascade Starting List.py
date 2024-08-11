import random
import matplotlib.pyplot as plt

count = 0
visited = []

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
    file = 'TextFiles/p2p-Gnutella08.txt'
    groups = 'TextFiles/Starting Nodes'

    data = open(groups, 'r')
    initialization = data.readline().split()

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

            ans[j].append(sum/100)

    print(ans)

    plt.plot(x, ans[0], linestyle="solid")
    plt.plot(x, ans[1], linestyle="dotted")
    plt.plot(x, ans[2], linestyle="dashed")

    plt.legend(["random", "most neighbors", "influence maximization"])
    plt.title("Independent Cascade 70% Probability")
    plt.xlabel("Starting Group Size")
    plt.ylabel("Infection Size")
    plt.show()