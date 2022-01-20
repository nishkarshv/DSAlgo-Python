import unittest

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    def dfs(self, array):
        array.append(self.name)
        for child in self.children:
            child.dfs(array)
        return array
    
class TestNode(unittest.TestCase):
    def test_case_1(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(graph.dfs([]), ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])