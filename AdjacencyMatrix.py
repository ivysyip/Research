def make_Matrice(file):
    data = open(file, 'r')
    initialization = data.readline().split()

    nodes = int(initialization[0])
    edges = int(initialization[1])

    length = nodes
    matrix = [[False for j in range(length)] for i in range(length)]

    count = 0

    for i in range(edges):
        edge = data.readline().split()

        start_node = int(edge[0])
        end_node = int(edge[1])

        matrix[start_node][end_node] = True

    return matrix

def check(list):
    count = 0
    nodes = len(list)

    for i in range(nodes):
        for j in range(len(list[i])):
            if list[i][j]:
                count += 1

    print(count)

if __name__ == '__main__':
    matrix = make_Matrice('TextFiles/p2p-Gnutella08.txt')
    check(matrix)