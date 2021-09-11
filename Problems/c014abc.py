"""
C - AtColor https://atcoder.jp/contests/abc014/tasks/abc014_3
いもす法
"""
import sys

# sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

from itertools import accumulate


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

    logger.debug("{}".format([]))

    imosu = [0] * 1000002
    for a, b in grid:
        imosu[a] += 1
        imosu[b + 1] += -1

    print(max(accumulate(imosu)))


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
0 2
2 3
2 4
5 6"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4
1000000 1000000
1000000 1000000
0 1000000
1 1000000"""
        output = """4"""
        self.assertIO(input, output)
