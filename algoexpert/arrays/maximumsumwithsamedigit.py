import unittest

class Test(unittest.TestCase):
    def test_case(self):
        input = [55, 23, 32, 46,88]
        generated = maximumsum(input)
        sumval = generated[2]
        print(generated[0], generated[1])
        output = 101
        self.assertEqual(output, 1)

def digitsum(n):
    sum = 0
    while n:
        sum+=(n%10)
        n = n//10
    return sum
    
def maximumsum(array):
    length = len(array)
    mp = {}
    res = -1
    x = 0
    y = 0
    for i in range(length):
        temp = digitsum(array[i])
        if temp not in mp:
            mp[temp] = 0
        if mp[temp]!=0:
            if array[i] + mp[temp] > res:
                x = array[i]
                y = mp[temp]
                res = array[i] + mp[temp]
        mp[temp] = max(array[i], mp[temp])

    return (x,y,res)
    