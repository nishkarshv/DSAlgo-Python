# Given an array of buildings and a direction that all of the building face, return an array of the indices of the building that can see the sunset.
# a building can see subset if it's strictly taller than all of the buildings taht come after it in the direction that it faces.
# hieghts are denoted by buildings[i], all faces same direction, direction is either EAST or WEST . 
# Input - buildings = [3,5,4,4,3,1,3,2]
#         direction = "EAST"
# Output - [1,3,6,7]  -- return indices

import unittest

def sunsetViews(buildings, direction):
    stack = []
    start = 0 if direction == "EAST" else len(buildings) - 1
    step = 1 if direction == "EAST" else -1
    i = start
    while i>=0 and i<len(buildings):
        buildingheight = buildings[i]
        while len(stack) > 0  and buildings[stack[-1]] <= buildingheight:
            stack.pop()
        stack.append(i)
        i+=step
    if direction == "WEST":
        return stack[::-1]
    return stack

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        buildings = [3,5,4,4,3,1,3,2]
        direction = "EAST"
        expected = [1,3,6,7]
        actual = sunsetViews(buildings, direction)
        self.assertEqual(actual, expected)