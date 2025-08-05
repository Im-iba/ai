from collections import deque
def bfs(graph, strat_node):
    visited=set()
    queue=deque()
    queue.append(strat_node)
    visited.add(strat_node)
    print("tranversal of the graph")
    while queue:
        current_node=queue.popleft()
        print(current_node, end=" ")

        for neighbour in graph.get(current_node,[]):
            if neighbour not in visited:
                queue.append(neighbour)
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}
bfs(graph,'A')