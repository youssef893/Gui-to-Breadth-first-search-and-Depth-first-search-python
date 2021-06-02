from collections import defaultdict


class GraphBFs:
    def __init__(self):
        self.graph = defaultdict(list)
        self.add_node()

    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)

    def add_node(self, ):
        self.add_edge(0, 1)
        self.add_edge(1, 0)
        self.add_edge(1, 2)
        self.add_edge(2, 1)
        self.add_edge(2, 0)
        self.add_edge(4, 0)
        self.add_edge(3, 0)
        self.add_edge(2, 3)

    def get_shortest_path(self, node, path, queue, visited, goal):
        if node not in visited:
            neighbours = self.graph[node]

            for neighbour in neighbours:
                shortest_path = list(path)
                shortest_path.append(neighbour)
                queue.append(shortest_path)

                if neighbour == goal:
                    print("Shortest path = ", *shortest_path)
                    return shortest_path
            visited.append(node)
        return

    def BFS(self, start, goal):
        visited = []
        queue = [[start]]

        if start == goal:
            return "Same Node"

        while queue:
            path = queue.pop(0)
            node = path[-1]
            shortest_path = self.get_shortest_path(node, path, queue, visited, goal)
            print(shortest_path)
            return shortest_path

    def DFS(self, start, goal, path, discovered):
        keys = list(self.graph.keys())
        start_index = keys.index(start)

        discovered[start_index] = True
        path.append(start)

        if start == goal:
            return True, list(path)

        for i in self.graph[start]:
            if not discovered[i]:
                if self.DFS(i, goal, path, discovered):
                    return True, list(path)

        path.pop()
        return False
