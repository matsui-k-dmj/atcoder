"""RMQ, セグメントツリー, セグ木
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
    """RMQ
    
    Returns:
        [type]: [description]
    """
    def __init__(self, h_list):

        # 簡単のために要素数を2のべき乗にしておく
        _n = len(h_list)
        self.n = 1
        while (self.n < _n):
            self.n = self.n * 2

        self.tree = [10**10 for _ in range(2 * self.n - 1)]

        for i, x in enumerate(h_list):
            self.update(i, x)

    def update(self, i, x):
        i = i + self.n - 1
        self.tree[i] = x

        # 親を更新
        while (i > 0):
            i = (i - 1) // 2
            self.tree[i] = min(self.tree[i * 2 + 1], self.tree[i * 2 + 2])

    def query(
        self,
        i_query_start,
        i_query_end,  # exclusive
        i_parent=0,
        i_parent_start=0,
        i_parent_end=None  # exclusive
    ):
        if i_parent_end is None:  # i_parent_end の 初期値
            i_parent_end = self.n

        if (i_query_end <= i_parent_start
                or i_parent_end <= i_query_start):  # クエリとレンジが重ならない
            return 10**10
        elif (i_query_start <= i_parent_start
              and i_parent_end <= i_query_end):  # クエリがレンジを完全に含む
            return self.tree[i_parent]
        else:  # 子供のminを返す
            return min(
                self.query(i_query_start, i_query_end, 2 * i_parent + 1,
                           i_parent_start,
                           (i_parent_start + i_parent_end) // 2),
                self.query(i_query_start, i_query_end, 2 * i_parent + 2,
                           (i_parent_start + i_parent_end) // 2, i_parent_end))


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    N, S, T = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    # grid = [[int(x) for x in sys.stdin.readline().split()]
    #         for _ in range(N)]  # int grid
    seg_tree = SegTree(h_list)

    print(seg_tree.query(S, T))


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
        input = """9 0 1
1 2 3 4 1 2 3 4 0"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9 1 4
1 2 3 4 1 2 3 4 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9 8 9
1 2 3 4 1 2 3 4 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """9 1 9
1 2 3 4 1 2 3 4 0"""
        output = """0"""
        self.assertIO(input, output)
