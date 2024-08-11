
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

        list[start_node].append(end_node)

    return list

if __name__ == '__main__':
    file = 'TextFiles/p2p-Gnutella08.txt'
    list = make_List(file)

    neighbors = [len(list[i]) for i in range(len(list))]
    N = 3
    res = sorted(range(len(neighbors)), key=lambda sub: neighbors[sub])[-N:]

    print(res)