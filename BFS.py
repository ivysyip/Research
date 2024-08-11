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

def BFS(list, node):
    queue = deque()
    visited = [False for i in range(len(list))]
    visited[node] = True
    queue.append(node)

    while len(queue) > 0:
        curr = queue.popleft()
        print(curr)
        for w in list[curr]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)

if __name__ == '__main__':
    list = make_List('TextFiles/BFS_DFS.txt')
    BFS(list, 0)