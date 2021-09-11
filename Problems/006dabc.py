"""
最長増加部分列 LIS
D - トランプ挿入ソート https://atcoder.jp/contests/abc006/tasks/abc006_4
"""
import sys

# sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

from bisect import bisect_left


def lis(c_list, INF=10e32):
    dp = [INF] * len(c_list)
    for c in c_list:
        i = bisect_left(dp, c)
        dp[i] = c

    return bisect_left(dp, INF), dp


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    c_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int
    # grid = [
    #     [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    # ]  # int grid

    logger.debug("{}".format([]))

    n_lis, dp = lis(c_list)

    print(len(c_list) - n_lis)


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
        input = """6
1
3
5
2
4
6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
5
4
3
2
1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
1
2
3
4
5
6
7"""
        output = """0"""
        self.assertIO(input, output)
