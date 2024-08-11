from collections import deque

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

def DFS_iterative(list, node):
    stack = deque()
    visited = [False for i in range(len(list))]
    print(node)
    visited[node] = True
    stack.append(node)

    while len(stack) > 0:
        v = stack.pop()

        if not visited[v]:
            print(v)
            visited[v] = True

        for w in list[v]:
            if not visited[w]:
                stack.append(w)

def DFS_recursive(list, node, visited=None):
    if visited is None:
        visited = []
    visited.append(node)
    print(node)

    for w in list[node]:
        if w not in visited:
            DFS_recursive(list, w, visited)

    return visited

if __name__ == '__main__':
    list = make_List('TextFiles/BFS_DFS.txt')
    DFS_iterative(list, 0)
    print('----------')
    #visited = [False for i in range(len(list))]
    DFS_recursive(list, 0)