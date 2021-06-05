from collections import defaultdict


class GraphBFs:
    def __init__(self):
        self.graph = defaultdict(list)
        self.add_node()
        self.visited = [False] * len(self.graph)

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
        queue = [[start]]

        # If the desired node is
        # reached
        if start == goal:
            print("Same Node")
            return

        # Loop to traverse the graph
        # with the help of the queue
        while queue:
            path = queue.pop(0)
            node = path[-1]

            # Condition to check if the
            # current node is not visited
            if node not in explored:
                neighbours = self.graph[node]

                # Loop to iterate over the
                # neighbours of the node
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    # Condition to check if the
                    # neighbour node is the goal
                    if neighbour == goal:
                        print("Shortest path = ", *new_path)
                        return new_path
                explored.append(node)

        return

    def DFS(self, start, goal, path):
        keys = list(self.graph.keys())
        start_index = keys.index(start)

        self.visited[start_index] = True
        path.append(start)

        if start == goal:
            return True, list(path)

        for i in self.graph[start]:
            if self.DFS(i, goal, path):
                print("insid DFS", path)
                return True, list(path)

        path.pop()
        return False, "No path"
