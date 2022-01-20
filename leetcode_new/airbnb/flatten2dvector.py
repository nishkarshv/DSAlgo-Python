class Vector2D(object):

    def __init__(self, a):
        def it():
            for line in a:
                for val in line:
                    self.size -= 1
                    yield val   
										
        self.it = it()
        self.size = sum(len(line) for line in a)

    def next(self):
        return next(self.it)

    def hasNext(self):
        return self.size
    

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()