# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.queue = []

    def read(self, buf, n):
        idx = 0
        while True:
            buf4 = [""] * 4
            l = read4(buf4)
            self.queue.extend(buf4)
            curr = min(len(self.queue), n - idx)
            for i in xrange(curr):
                buf[idx] = self.queue.pop(0)
                idx += 1
            if curr == 0:
                break
        return idx

    def read(self, buf: List[str], n: int) -> int:
        idx = 0

        while idx < n:
            if self.q:
                buf[idx] = self.q.pop(0)
                idx += 1

            else:
                buf4 = [""] * 4
                read = read4(buf4)
                if read == 0:
                    return idx
                self.q += buf4

        return idx