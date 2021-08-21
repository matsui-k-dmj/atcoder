"""セグメントツリー, セグ木
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
class SegTree:
    def __init__(self, N):

        self.default = (1, 0)

        # 簡単のために要素数を2のべき乗にしておく
        _n = N
        self.n = 1
        while (self.n < _n):
            self.n = self.n * 2

        self.tree = [self.default for _ in range(2 * self.n - 1)]

    def update(self, i, x):
        i = i + self.n - 1
        self.tree[i] = x

        # 親を更新
        while (i > 0):
            i = (i - 1) // 2
            al, bl = self.tree[i * 2 + 1]
            ar, br = self.tree[i * 2 + 2]
            self.tree[i] = (ar * al, ar * bl + br)


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    N, M = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    grid = [[float(x) for x in sys.stdin.readline().split()]
            for _ in range(M)]  # int grid

    logger.debug('{}'.format([]))

    seg = SegTree(N)
    _min = 1
    _max = 1
    for p, a, b in grid:
        p = int(p) - 1
        seg.update(p, (a, b))
        a_root, b_root = seg.tree[0]
        t = a_root + b_root
        if t < _min:
            _min = t
        if t > _max:
            _max = t
    print(_min)
    print(_max)


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
        input = """1 1
1 1 0"""
        output = """1
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
2 -1 1
2 1 0.5"""
        output = """0
1.5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 5
1 -0.8 0.5
2 0.72 -0.21
3 1 0.8
4 0.3 0.4142
3 1 0.8"""
        output = """-0.426
1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 10
6 0.5674 -1
3 -0.432 0.1235
8 0.92 0
4 -0.673 0.12578
6 0.986 -0.567
1 0.11111 1
10 0.98765 -0.1234
10 0.18543 -0.16532
9 -0.756 0.54849
2 -1 0.74436"""
        output = """-1.175043
1"""
        self.assertIO(input, output)
