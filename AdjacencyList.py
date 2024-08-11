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

def check(list):
    count = 0
    nodes = len(list)

    for i in range(nodes):
        count += len(list[i])

    print(count)

if __name__ == '__main__':
    list = make_List('TextFiles/p2p-Gnutella08.txt')
    check(list)