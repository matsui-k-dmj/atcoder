"""最長増加部分列 LIS
"""

import sys

sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

# from collections import defaultdict
# d = defaultdict(list)

# from itertools import combinations
# comb = combinations(range(N), 2)

# 累積和
# from itertools import accumulate
# _list = list(accumulate(a_list)

import bisect

from typing import List


def lis(N: int, h_list: List[int], INF=10 ** 10) -> int:
    dp = [INF for _ in range(N)]

    for j in range(N):
        h = h_list[j]
        i = bisect.bisect_left(dp, h)
        dp[i] = h

    i = bisect.bisect_left(dp, INF)

    return i


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    # grid = [[int(x) for x in sys.stdin.readline().split()]
    #         for _ in range(N)]  # int grid

    logger.debug("{}".format([]))

    print(lis(N, h_list))


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

    def test_入力例_1(self):
        input = """5
3 1 5 4 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
1 2 3 4 5 6"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
7 6 5 4 3 2 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """20
19 11 10 7 8 9 17 18 20 4 3 15 16 1 5 14 6 2 13 12"""
        output = """6"""
        self.assertIO(input, output)
