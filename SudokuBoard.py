from Graph_Package.Graph import Graph

class SudokuBoard(object):
    def __init__(self, grid):
        self.graph = Graph(grid)
        self.resolution = []

    def print(self):
        print("-" * 37)
        for i, row in enumerate(self.resolution):
            print(("|" + " {}   {}   {} |" * 3).format(*[x if x != 0 else " " for x in row]))
            if i == 8:
                print("-" * 37)
            elif i % 3 == 2:
                print("|" + "---+" * 8 + "---|")
            else:
                print("|" + "   +" * 8 + "   |")

    def solve(self):
        self.graph.DSatur()
        for i in range(9):
            line = []
            for j in range(9):
                line.append(self.graph.nodes[i * 9 + j].color.value)
            self.resolution.append(line)

