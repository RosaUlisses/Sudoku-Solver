from Graph_Package.Color import Color
from math import inf


class Node(object):
    def __init__(self, color, row, column):
        self.adjacents = set()
        self.color = color
        self.id = (row, column)

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return self is other

    def setEdge(self, node):
        self.adjacents.add(node)

    def getSaturation(self):
        saturation = 0
        adjacent_colors = set()

        for node in self.adjacents:
            if(node.color not in adjacent_colors and node.color != Color.NONE):
                adjacent_colors.add(node.color)
                saturation += 1

        return saturation

    def getUncolloredDegree(self):

        saturation = 0

        for node in self.adjacents:
            if (node.color == Color.NONE):
                saturation += 1

        return saturation

    def generateColor(self):

        colors = {Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.PINK, Color.BLACK, Color.WHITE, Color.PURPLE,
                  Color.BROWN}

        for node in self.adjacents:
            if (node.color in colors):
                colors.remove(node.color)

        lowest_color_value = inf
        lowest_color = Color.NONE

        for color in colors:
            if (color.value < lowest_color_value):
                lowest_color = color.value
                lowest_color = color

        return lowest_color
