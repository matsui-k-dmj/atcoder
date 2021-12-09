import sys
# sys.setrecursionlimit(4200000)


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# import math

# from collections import defaultdict


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, A, B = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    P, Q, R, S = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    H = Q - P + 1
    W = S - R + 1

    grid = [["."] * W for i in range(H)]

    max1 = max(1 - A, 1 - B)
    min1 = min(N - A, N - B)
    max2 = max(1 - A, B - N)
    min2 = min(N - A, B - 1)

    ik_min = max(P - A, max1)
    ik_max = min(Q - A, min1)

    jk_min = max(R - B, max1)
    jk_max = min(S- B , min1)

    mi = max(ik_min, jk_min)
    ma = min(ik_max, jk_max)

    for k in range(mi, ma + 1):
        if 0 <= A + k - P <= H - 1 and 0 <= B + k - R <= W -1:
            grid[A + k - P][B + k - R] = "#"

    ik_min = max(P - A, max2)
    ik_max = min(Q - A, min2)

    jk_min = max(R - B, - max2)
    jk_max = min(S - B, - min2)

    mi = max(ik_min, - jk_min)
    ma = min(ik_max, - jk_max)
    
    for k in range(mi, ma + 1):
        i = A + k - P
        j =  B - k - R
        if 0 <= i  <= H -1 and 0 <= B - k - R <= W - 1:
            grid[i][j] = "#"
        


    for row in grid:
        print("".join(row))



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
        input = """5 3 2
1 5 1 5"""
        output = """...#.
#.#..
.#...
#.#..
...#."""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 3 3
4 5 2 5"""
        output = """#.#.
...#"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000000000000 999999999999999999 999999999999999999
999999999999999998 1000000000000000000 999999999999999998 1000000000000000000"""
        output = """#.#
.#.
#.#"""
        self.assertIO(input, output)


