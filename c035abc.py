"""区間に対する加算, SegTree
imos法使うべき
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

# from functools import lru_cache
# @lru_cache(maxsize=None)
# def setUp(self):
#     dp.cache_clear()


class SegTree:
    def __init__(self, n):

        # 簡単のために要素数を2のべき乗にしておく
        _n = n
        self.n = 1
        while (self.n < _n):
            self.n = self.n * 2

        self.tree = [0 for _ in range(2 * self.n - 1)]

        # 要素数 n
        # SegTreeの配列の長さ 2 * n - 1
        # 親ノードの数 n - 1, 0 から n -1 (exclusive)
        # leaf ノードの 数 n, n - 1 から 2 * n - 1

    def reverse(
        self,
        i_left,  # inclusive
        i_right,  # inclusive
        i_parent=0,
        i_parent_start=0,
        i_parent_end=None):
        if i_parent_end is None:
            i_parent_end = self.n

        # 完全に含まない
        if i_parent_end <= i_left or i_right < i_parent_start:
            return
        # reverseの区間がノードを完全に含むなら、そこに加算
        elif i_left <= i_parent_start and i_parent_end - 1 <= i_right:
            self.tree[i_parent] += 1
        else:
            self.reverse(i_left, i_right, 2 * i_parent + 1, i_parent_start,
                         (i_parent_start + i_parent_end) // 2)
            self.reverse(i_left, i_right, 2 * i_parent + 2,
                         (i_parent_start + i_parent_end) // 2, i_parent_end)

    def query(self, i_parent):

        # leaf まで来てる
        if i_parent >= self.n - 1:
            return [self.tree[i_parent]]

        ret_list = self.query(2 * i_parent + 1) + self.query(2 * i_parent + 2)

        a = self.tree[i_parent]
        return [x + a for x in ret_list]


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    N, Q = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    grid = [[int(x) - 1 for x in sys.stdin.readline().split()]
            for _ in range(Q)]  # int grid

    logger.debug('{}'.format([]))

    seg = SegTree(N)

    for i_left, i_right in grid:
        seg.reverse(i_left, i_right)

    ret_list = seg.query(0)

    print(''.join([str(r % 2) for r in ret_list[:N]]))


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
        input = """5 4
1 4
2 5
3 3
1 5"""
        output = """01010"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 8
1 8
4 13
8 8
3 18
5 20
19 20
2 7
4 9"""
        output = """10110000011110000000"""
        self.assertIO(input, output)
