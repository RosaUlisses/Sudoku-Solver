from Graph_Package.Node import Node
from Graph_Package.Color import Color
from Graph_Package.Color import colors
from math import inf

class Graph(object):
    def __init__(self, grid):

        sudoku_grid = []

        for i, line in enumerate(grid):
            aux = []
            for j, value in enumerate(line):
                aux.append(Node(colors[value], i, j))
            sudoku_grid.append(aux)

        for i in range(9):
            for j in range(9):

                for x in range(9):
                    if (sudoku_grid[i][j] != sudoku_grid[i][x] and sudoku_grid[i][j].color == Color.NONE):
                        sudoku_grid[i][j].setEdge(sudoku_grid[i][x])

                for y in range(9):
                    if (sudoku_grid[i][j] != sudoku_grid[y][j] and sudoku_grid[i][j].color == Color.NONE):
                        sudoku_grid[i][j].setEdge(sudoku_grid[y][j])

                x_min, y_min = int(i / 3) * 3, int(j / 3) * 3
                x_max, y_max = x_min + 3, y_min + 3
                for x in range(x_min, x_max):
                    for y in range(y_min, y_max):
                        if (sudoku_grid[i][j] != sudoku_grid[x][y] and sudoku_grid[i][j].color == Color.NONE):
                            sudoku_grid[i][j].setEdge(sudoku_grid[x][y])

        self.nodes = [value for line in sudoku_grid for value in line]



    def color_node(self, node, uncolored_nodes):

        uncolored_nodes.remove(node)

        adjacents = set()

        for value in uncolored_nodes:
            if(node in value.adjacents):
                value.adjacents.remove(node)
                adjacents.add(value)

        color = node.generateColor()
        node.color = color
        node.adjacents.clear()

        for value in adjacents:
            value.adjacents.add(node)


    def DSatur(self):

        uncolored_nodes = set()
        for node in self.nodes:
            if(node.color == Color.NONE):
                uncolored_nodes.add(node)

        while(len(uncolored_nodes)):

            highest_saturation = -inf
            highest_saturation_node = None

            for node in self.nodes:
                if(node.color != Color.NONE): continue
                saturation = node.getSaturation()
                if(saturation > highest_saturation):
                    highest_saturation = saturation
                    highest_saturation_node = node
                elif(saturation == highest_saturation):
                    if(node.getUncolloredDegree()):
                        highest_saturation_node = node

            highest_saturation_node.getSaturation()
            self.color_node(highest_saturation_node, uncolored_nodes)



    def print(self):

        matrix = []

        k = 0

        for i in range(0, 9):
            list = []
            for j in range(0, 9):
                list.append(self.nodes[k].color.value)
                k += 1
            matrix.append(list)

