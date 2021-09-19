"""
2分探索
"""

import sys
import math

# # sys.setrecursionlimit(4100000)

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int

    grid = [
        [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    ]  # int grid

    # logger.debug("{}".format([]))

    def cost(x):
        tmp = sorted([(x - h) // s for h, s in grid])
        return all([i <= max_n for i, max_n in enumerate(tmp)])

    lb = 0
    ub = 10 ** 15

    while ub - lb > 1:
        mid = (ub + lb) // 2
        if cost(mid):
            ub = mid
        else:
            lb = mid

    print(ub)


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

    def test_入力例1(self):
        input = """4
5 6
12 4
14 7
21 2"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6
100 1
100 1
100 1
100 1
100 1
1 30"""
        output = """105"""
        self.assertIO(input, output)
