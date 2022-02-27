from collections import defaultdict
from collections import deque


class Graph(object):
    """ Graph data structure, undirected by default. Has to be a connected Graph """

    def __init__(self, connections=None, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self._number_of_edges = 0 # in a directional graph each edge is counted. so (1,2) and (2,1) are 2 different edges
        if connections is not None:
            self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)
            

    def number_of_edges(self):
        return self._number_of_edges
    
    def number_of_nodes(self):
        return len(self._graph)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)       # set.add()
        self._number_of_edges += 1
        if not self._directed:
            self._graph[node2].add(node1)          

    def remove(self, node):
        """ Remove all references to node """

        for n, group_of_neighbors in self._graph.items():
            try:
                group_of_neighbors.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def dfs(self, s):
        """ go over the graph in dfs order, starting from node s """
        dfs_path = []
        stack = []
        visited = defaultdict(bool)
        stack.append(s)
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                dfs_path.append(node)
            neighbors = self._graph[node]
            for neighbor in neighbors:
                if not visited[neighbor]:
                    stack.append(neighbor)
        return dfs_path

    def bfs(self, s):
        bfs_path = []
        # Initializing a queue
        queue = deque()
        visited = defaultdict(bool)
        queue.append(s)
        while queue:
            node = queue.popleft()
            if not visited[node]:
                visited[node] = True
                bfs_path.append(node)
            neighbors = self._graph[node]
            for neighbor in neighbors:
                if not visited[neighbor]:
                    queue.append(neighbor)
        return bfs_path
        

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))





if __name__ == "__main__":
    G = Graph()
    G.add(0,4)
    G.add(0,2)
    G.add(2,4)
    G.add(1,2)
    G.add(3,1) # order of nodes doesnt matter in edge
    print(G)
    print(G.dfs(2))
    print(G.bfs(2))
    print(G.number_of_edges())
    print(G.number_of_nodes())
    
    
