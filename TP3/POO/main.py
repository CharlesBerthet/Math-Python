from math import *
import matplotlib.pyplot as plt

class Liste:
    def __init__(self):
        self.liste = []

    def ajouter(self, element):
        self.liste.append(element)

class Graph:
    def __init__(self):
        self.graph = []

    def suite(self, n):
        return log(1+1/n)
    
    def graph(self):
        x = [i for i in range(1, 10)]
        y = [self.suite(i) for i in x]
        plt.plot(x, y)
        plt.show()

graph = Graph()

graph.graph()





