import math


class Bitset:
    def __init__(self, a_list=None):
        self.set = 0
        if a_list is not None:
            for a in a_list:
                self.add(a)

    def add(self, i):
        self.set = self.set | (1 << i)

    def remove(self, i):
        self.set = self.set & ~(1 << i)

    def find(self, i):
        return (self.set >> i) & 1

    def union(self, a_set):
        bs = Bitset()
        bs.set = self.set | a_set.set
        return bs

    def intersect(self, a_set):
        bs = Bitset()
        bs.set = self.set & a_set.set
        return bs

    def enumerate(self):
        x = self.set & -self.set
        while (x):
            yield int(math.log2(x))
            x = self.set & (~self.set + (x << 1))
