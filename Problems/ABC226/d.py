import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from math import gcd

from itertools import combinations


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # a_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int

    grid = [
        [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    ]  # int grid

    s = set()
    for i, j in combinations(range(N), 2):
        xi = tuple(grid[i])
        xj = tuple(grid[j])
        d = gcd(abs(xi[0] - xj[0]), abs(xi[1] - xj[1]))
        s.add(((xi[0] - xj[0]) // d, (xi[1] - xj[1]) // d))
        s.add((-(xi[0] - xj[0]) // d, -(xi[1] - xj[1]) // d))

    print(len(s))


if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest hoge.py
# pypy3 -m unittest hoge.py

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

    def test_入力例_1(self):
        input = """3
1 2
3 6
7 4"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 2
2 2
4 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
0 0
0 1000000000
1000000000 0
1000000000 1000000000"""
        output = """8"""
        self.assertIO(input, output)
