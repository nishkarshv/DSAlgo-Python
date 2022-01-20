import unittest

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def addChild(self,name):
        self.children.append(Node(name))
        return self
    def bfs(self, array):
        q = [self]
        while len(q)>0:
            current = q.pop(0)
            array.append(current.name)
            for child in current.children:
                q.append(child)
        return array

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(graph.bfs([]), ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])
