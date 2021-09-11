"""
提出 #25734082 - 全国統一プログラミング王決定戦本戦 https://atcoder.jp/contests/nikkei2019-final/submissions/25734082
累積和
"""
import sys

# sys.setrecursionlimit(4100000)

import math
from itertools import accumulate

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int
    # grid = [
    #     [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    # ]  # int grid

    logger.debug("{}".format([]))

    c_list = list(accumulate(a_list))
    c_list = [0] + c_list
    for k in range(1, N + 1):
        print(max([c_list[i + k] - c_list[i] for i in range(N - k + 1)]))


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
4 1 3 3"""
        output = """4
6
8
11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
10 20 30 40 50"""
        output = """50
90
120
140
150"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
61049214 115057849 356385814 932678664 505961980 877482753 476308661 571830644 210047210 873430114"""
        output = """932678664
1438640644
2316123397
2792432058
3364262702
3720648516
4447740026
4804125840
4919183689
4980232903"""
        self.assertIO(input, output)
