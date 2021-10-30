import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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

    # logger.debug("{}".format([]))

    count = 0
    for indexes in combinations(range(N), 3):
        p0, p1, p2 = grid[indexes[0]], grid[indexes[1]], grid[indexes[2]]
        if p0[0] == p1[0]:
            if p2[0] == p0[0]:
                continue
            else:
                count += 1
        else:
            y = (p2[1] - p0[1]) * (p1[0] - p0[0])
            x = (p1[1] - p0[1]) * (p2[0] - p0[0])
            if y == x:
                continue
            else:
                count += 1

    print(count)


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
        input = """4
0 1
1 3
1 1
-1 -1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20
224 433
987654321 987654321
2 0
6 4
314159265 358979323
0 0
-123456789 123456789
-1000000000 1000000000
124 233
9 -6
-4 0
9 5
-7 3
333333333 -333333333
-9 -1
7 -10
-1 5
324 633
1000000000 -1000000000
20 0"""
        output = """1124"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
0 0
1 0
-1 0
"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3
0 0
0 1
0 -1
"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """3
0 0
1 1000000000
-1 -1000000000
"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_6(self):
        input = """3
1 0
1 1000000000
-1 -1000000000
"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_7(self):
        input = """3
2 1000000000
1 1000000000
-1 -1000000000
"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_8(self):
        input = """3
1000000000 1
-1000000000 -1
0 0
"""
        output = """0"""
        self.assertIO(input, output)
