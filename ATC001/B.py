"""
Union Find
"""

import sys
sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

class UnionFindTree(object):
    def __init__(self, N):
        self.parent_list = [i for i in range(N)]
        self.rank_list = [0] * N

    def find(self, i):
        if self.parent_list[i] == i:
            return i
        else:
            p = self.find(self.parent_list[i])
            self.parent_list[i] = p
            return p

    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank_list[root_x] > self.rank_list[root_y]:
            # root_x のほうが深いので、root_y の 親を root_x にする
            self.parent_list[root_y] = root_x

        else:
            self.parent_list[root_x] = root_y

            if self.rank_list[root_x] == self.rank_list[root_y]:
                self.rank_list[root_x] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

def resolve():
    N, Q = [int(x) for x in sys.stdin.readline().split()]
    q_list = [[int(x) for x in sys.stdin.readline().split()] for _ in range(Q)]

    logger.debug('{} {}'.format(N, Q))

    uft = UnionFindTree(N)

    for p, a, b in q_list:
        if p == 0:
            uft.unite(a, b)
        else:
            print("Yes" if uft.is_same(a, b) else "No")


if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest template/template.py で実行できる
# pypy3 -m unittest template/template.py で実行できる

import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例1(self):
        input = """8 9
0 1 2
0 3 2
1 1 3
1 1 4
0 2 4
1 4 1
0 4 2
0 0 0
1 0 0"""
        output = """Yes
No
Yes
Yes"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1 1
1 0 0"""
        output = """Yes"""
        self.assertIO(input, output)