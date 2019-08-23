#!/usr/bin/env python3

def dfs_rec(list_path, graph, start, dict_visited):
    if dict_visited[start] == False:
        dict_visited[start] = True
        list_path.append(start)
        for end in graph[start]:
            dfs_rec(list_path, graph, end, dict_visited)
    return

def bfs_rec(list_path, graph, list_start, dict_visited):
    list_next = []
    for start in list_start:
        if dict_visited[start] == False:
            dict_visited[start] = True
            list_path.append(start)
            for end in graph[start]:
                if dict_visited[end] == False:
                    list_next.append(end)
    if bool(list_next):
        bfs_rec(list_path, graph, list_next, dict_visited)
    return
    

def main():
    graph = {'A': ['B', 'C'], 
             'B': ['A', 'D', 'E'], 
             'C': ['A', 'F'], 
             'D': ['B'], 
             'E': ['B', 'F'], 
             'F': ['C', 'E']}
    start = 'A'
    list_fs = []
    dict_visited = {'A': False,
                    'B': False,
                    'C': False,
                    'D': False,
                    'E': False,
                    'F': False}
    # recursive DFS
    dfs_rec(list_fs, graph, start, dict_visited)
    print("recursive DFS = {}".format(list_fs))
    # stack DFS
    list_fs.clear()
    dict_visited = {'A': False,
                    'B': False,
                    'C': False,
                    'D': False,
                    'E': False,
                    'F': False}
    start = 'A'
    stack = [start]
    while bool(stack):
        start = stack.pop()
        if dict_visited[start] == False:
            dict_visited[start] = True
            list_fs.append(start)
            for ii in range(-1, -len(graph[start])-1, -1):
                stack.append(graph[start][ii])
    print("stack DFS = {}".format(list_fs))

    # recursive BFS
    list_fs.clear()
    dict_visited = {'A': False,
                    'B': False,
                    'C': False,
                    'D': False,
                    'E': False,
                    'F': False}
    start = 'A'
    bfs_rec(list_fs, graph, [start], dict_visited)
    print("recursive BFS = {}".format(list_fs))
    # queue BFS
    list_fs.clear()
    dict_visited = {'A': False,
                    'B': False,
                    'C': False,
                    'D': False,
                    'E': False,
                    'F': False}
    start = 'A'
    queue = [start]
    while bool(queue):
        start = queue.pop(0)
        if dict_visited[start] == False:
            list_fs.append(start)
            dict_visited[start] = True
            for end in graph[start]:
                queue.append(end)
    print("queue DFS = {}".format(list_fs))
    return

if __name__ == "__main__":
    main()