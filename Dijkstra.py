import math

class Edge:
    def __init__(self, v, w):
        self.end_node = v
        self.weight = w

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
        weight = int(edge[2])

        list[start_node].append(Edge(end_node, weight))
        list[end_node].append(Edge(start_node, weight))

    return list

def dijkstra(list, node):
    N = []
    dist = [math.inf for i in range(len(list))]
    prev = [None for i in range(len(list))]
    Q = []

    for v in range(len(list)):
        if v != node:
            contains = False
            weight = 0

            for edge in list[node]:
              if edge.end_node == v:
                  contains = True
                  weight = edge.weight

            if contains:
                dist[v] = weight
                prev[v] = node

            Q.append(v)

    while len(Q) > 0:
        min_d = math.inf
        u = None
        for n in Q:
            if (dist[n] < min_d):
                u = n
                min_d = dist[n]

        Q.remove(u)
        N.append(u)

        for v in Q:
            contains = False
            weight = 0

            for edge in list[u]:
                if edge.end_node == v:
                    contains = True
                    weight = edge.weight

            if contains:
                alt = dist[u] + weight

                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    return dist, prev


if __name__ == '__main__':
    list1 = make_List('TextFiles/Dijkstra1.txt')
    dist1, prev1 = dijkstra(list1, 0)
    print(dist1)
    print(prev1)
    list2 = make_List('TextFiles/Dijkstra2.txt')
    dist2, prev2 = dijkstra(list2, 0)
    print(dist2)
    print(prev2)