testcases = [
    [3, [0, 1, 1, 2, 2, 3]],
    [5, [0, 1, 1, 2, 2, 3, 2, 4, 4, 0]],
    [5, [0, 1, 1, 2, 2, 3, 2, 4, 2, 5, 2, 6, 6, 0]],
    [5, [0, 1, 1, 2, 2, 3, 3, 4, 3, 5, 3, 6, 6, 0]],
    [0, []],
    [2, [0, 1, 1, 0]]
]

gvisited = []


def search(graph, visited, next):
    if next in visited:
        return True

    visited.append(next)
    gvisited.append(next)
    if next in graph:
        for i in graph[next]:
            if search(graph, visited, i) == True:
                return True

    return False

# def isCyclic(edges) -> bool:
#    graph = {}
#
#    for v, o in edges:
#        if v not in graph:
#            graph[v] = [o]
#        else:
#            graph[v].append(o)
#
#    for k in graph:
#        if k not in gvisited:
#            gvisited.append(k)
#            for i in graph[k]:
#                if search(graph, [k], i) == True:
#                    return True
#
#    return False
#


def dfs(gvisited, graph, k):
    visited = [k]
    stack = [k]

    while len(stack) > 0:
        # if node k exits and unsearched children exist
        for ci in range(len(graph[k])):
            n = graph[k][ci]
            # mark as visited.
            visited.append(n)
            gvisited.append(n)
            # if a child of node k is in the graph
            # then keep searching
            if n in graph:
                stack.append(n)
                # if a child of node k is visited, then it means the graph is cyclic.
                # so return True
                for c in graph[n]:
                    if c in visited:
                        return True
                k = n
            else:
                stack.pop()

    return False


def isCyclic(edges) -> bool:
    graph = {}

    for v, o in edges:
        if v not in graph:
            graph[v] = [o]
        else:
            graph[v].append(o)

    # gvisited is for optimisation purpose
    # in case two completely separated graph is given,
    # skip alread searched graph if node k is visited already
    gvisited = []
    for k in graph:
        if k not in gvisited:
            if dfs(gvisited, graph, k) == True:
                return True

    return False


if __name__ == "__main__":
    for n in testcases:
        gvisited = []
        egdes = [(n[1][i], n[1][i+1]) for i in range(0, len(n[1]), 2)]
        print(isCyclic(egdes))
