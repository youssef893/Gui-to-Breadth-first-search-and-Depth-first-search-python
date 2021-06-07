import tkinter as tk
from tkinter import *
from Search_Algorithms import Graph
import random
from collections import deque

g = Graph()
path = deque()


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        # Creating elements
        self.start_label = tk.Label(self, text="Start Node", font=("Helvetica", 20))
        self.start = tk.Entry(self, textvariable=tk.StringVar(), font=('calibre', 20, 'normal'))
        self.end_label = tk.Label(self, text="End Node", font=("Helvetica", 20))
        self.end = tk.Entry(self, textvariable=tk.StringVar(), font=('Helvetica', 20, 'normal'))
        self.bfs_btn = tk.Button(self, text="BFS", font=('Helvetica', 20, 'normal'),
                                 command=lambda m='bfs': self.draw_graph(m))
        self.button_clear = tk.Button(self, text="Clear", font=('Helvetica', 20, 'normal'),
                                      command=self.clear_all)
        self.canvas = tk.Canvas(self, width=1000, height=700, bg="white")
        self.text = tk.Label(self, text="", font=("Helvetica", 20))
        self.dfs_btn = tk.Button(self, text="DFS", font=('Helvetica', 20, 'normal'),
                                 command=lambda m='dfs': self.draw_graph(m))
        self.start_grid()

    def start_grid(self):
        # Grid structure
        self.start_label.grid(row=0, column=0, pady=2, padx=2)
        self.start.grid(row=0, column=1, pady=2, padx=10)
        self.end_label.grid(row=1, column=0, pady=2, padx=2)
        self.end.grid(row=1, column=1, pady=2, padx=10)
        self.bfs_btn.grid(row=2, column=0, pady=0, padx=0)
        self.dfs_btn.grid(row=2, column=1, pady=0, padx=0)
        self.button_clear.grid(row=2, column=2, pady=2, padx=8)
        self.canvas.grid(row=4, column=3, pady=50, padx=50)
        self.text.grid(row=3, column=1)

    def clear_all(self):
        # clear input, canvas and enable buttons
        self.start.delete(0, 'end')
        self.end.delete(0, 'end')
        self.bfs_btn.configure(state=NORMAL)
        self.dfs_btn.configure(state=NORMAL)
        self.canvas.delete("all")
        self.text.configure(text='')

        path.clear()

    def draw_circle(self, x, y, rad):
        self.canvas.create_oval(x - rad, y - rad, x + rad, y + rad, width=3, fill='white')

    def check_shortest_path(self, shortest_path):
        # check there is a shortest path between 2 nodes or not
        if shortest_path is None:
            self.text.configure(text='There is no path')
            return True
        else:
            return False

    def get_shortest_path(self, node1, node2, shortest_path):
        # check if node1 and node2 are in shortest_path
        bool1, bool2 = False, False
        if not self.check_shortest_path(shortest_path):
            for i in shortest_path:
                if node1 == i:
                    bool1 = True
                    break
            for i in shortest_path:
                if node2 == i:
                    bool2 = True
                    break
        # if nodes in shortest path set text by shortest path
            if bool1 and bool2:
                self.text.configure(text=shortest_path)
                return True
            elif shortest_path == "Same Node":
                self.text.configure(text="Same Node")
                return False
            else:
                return False
        return False

    @staticmethod
    def check_digits(start, goal, btn):
        # change input to integer if it is digits
        if start.strip().isdigit():
            start = int(start)
            goal = int(goal)
        # call bfs function if btn is bfs and else dfs
        if btn == 'bfs':
            shortest_path = g.bfs(start, goal)
        else:
            _, shortest_path = g.DFS(start, goal, path)

        return shortest_path

    def draw_lines(self, keys, coordinates, values, shortest_path):
        colored = []
        for i in range(len(keys)):
            for j in range(len(values[i])):
                # get index of next node to draw arrow
                index = keys.index(values[i][j])
                condition = self.get_shortest_path(keys[i], keys[index], shortest_path)
                # if there is a shortest path, it will change its color to red
                if condition and keys[i] not in colored:
                    colored.append(keys[i])
                    self.canvas.create_line(coordinates[i][0], coordinates[i][1] + 10,
                                            coordinates[index][0], coordinates[index][1] + 10,
                                            width=2, arrow=tk.LAST, fill="red")
                else:
                    self.canvas.create_line(coordinates[i][0], coordinates[i][1] + 10,
                                            coordinates[index][0], coordinates[index][1] + 10,
                                            width=2, arrow=tk.LAST)

    def get_data(self, coordinates, keys, btn):
        values = list(g.graph.values())
        # get data from entries
        start = self.start.get()
        goal = self.end.get()
        shortest_path = self.check_digits(start, goal, btn)
        self.draw_lines(keys, coordinates, values, shortest_path)

    def draw_graph(self, btn):
        keys = list(g.graph.keys())
        coordinates = []
        for i in range(len(g.graph)):
            # get coordinates of each node
            x = random.randrange(30, 950)
            y = random.randrange(30, 650)
            coordinates.append((x, y))
            self.draw_circle(x, y, 30)
            self.canvas.create_text(x, y, fill="black", font="Helvetica", text=keys[i])

        self.get_data(coordinates, keys, btn)
        self.bfs_btn.configure(state=DISABLED)
        self.dfs_btn.configure(state=DISABLED)


if __name__ == '__main__':
    app = App()
    mainloop()
