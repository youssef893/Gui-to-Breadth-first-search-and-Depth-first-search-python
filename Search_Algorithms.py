from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.add_node()
        self.visited = [False] * len(self.graph)
        self.num_nodes = len(self.graph)

    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)

    def add_node(self, ):
        self.add_edge(0, 1)
        self.add_edge(1, 2)
        self.add_edge(2, 3)
        self.add_edge(3, 4)
        self.add_edge(4, 5)
        self.add_edge(5, 6)
        self.add_edge(6, 7)
        self.add_edge(7, 8)
        self.add_edge(8, 9)
        self.add_edge(9, 10)
        self.add_edge(10, 0)

    def bfs(self, start, goal):
        explored = []
        queue = [[start]]  # add start node to queue

        if start == goal:  # Check if start equal node
            print("Same Node")
            return "Same Node"

        # Loop to traverse the graph
        # with the help of the queue
        while queue:
            path = queue.pop(0)  # get first element of queue
            node = path[-1]  # node equal last element in path

            # Condition to check if the
            # current node is not visited
            if node not in explored:
                neighbours = self.graph[node]  # get values of this node
                # Loop to iterate over the
                # neighbours of the node
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)  # add neighbour to new path
                    queue.append(new_path)
                    # check if goal is reached return shortest path
                    if neighbour == goal:
                        print("Shortest path = ", *new_path)
                        return new_path
                explored.append(node)  # add visited node

    def DFS(self, start, goal, path):
        path.append(start)  # add start node to path
        if start == goal:
            return True, 'Same Node'
        elif goal not in self.graph:
            return True, "No Path"

        for i in self.graph[start]:  # get values of this node
            if self.DFS(i, goal, path):  # check if goal is reached return path
                self.num_nodes -= 1
                print("insid DFS", path)
                return True, list(path)

