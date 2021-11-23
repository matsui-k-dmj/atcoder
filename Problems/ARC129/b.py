import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import math


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ

    grid = [
        [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    ]  # int grid

    max_l = 0
    min_r = 10 ** 9
    for l, r in grid:
        if max_l < l:
            max_l = l
        if min_r > r:
            min_r = r

        if max_l <= min_r:
            print(0)
        else:
            print(math.ceil((max_l - min_r) / 2))


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
1 3
2 4
5 6"""
        output = """0
0
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
64 96
30 78
52 61
18 28
9 34
42 86
11 49
1 79
13 59
70 95"""
        output = """0
0
2
18
18
18
18
18
18
21"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
1 2
2 3
"""
        output = """0
0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2
1 2
3 4
"""
        output = """0
1"""
        self.assertIO(input, output)
