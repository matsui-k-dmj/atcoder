"""累積和 セグ木
転倒数

Returns:
    [type]: [description]
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


# 累積和 セグ木
class SegTree:
    def __init__(self, N):

        self.default = 0
        # 簡単のために要素数を2のべき乗にしておく
        _n = N
        self.n = 1
        while (self.n < _n):
            self.n = self.n * 2

        self.tree = [self.default for _ in range(2 * self.n - 1)]

    def update(self, i, x=1):
        i = i + self.n - 1
        self.tree[i] += x

        # 親を更新
        while (i > 0):
            i = (i - 1) // 2
            l = self.tree[i * 2 + 1]
            r = self.tree[i * 2 + 2]
            self.tree[i] = l + r

    def query(self,
              i_query_start,
              i_query_end,
              i_parent=0,
              i_parent_start=0,
              i_parent_end=None):
        if i_parent_end is None:
            i_parent_end = self.n

        if i_parent > self.n - 1:
            return self.default
        if (i_query_end <= i_parent_start
                or i_parent_end < i_query_start):  # クエリとレンジが重ならない
            return self.default
        elif (i_query_start <= i_parent_start
              and i_parent_end <= i_query_end):  # クエリがレンジを完全に含む
            return self.tree[i_parent]
        else:
            return self.query(i_parent_start, i_query_end, 2 * i_parent + 1,
                           i_parent_start, (i_parent_start + i_parent_end) // 2) + \
                self.query(i_parent_start, i_query_end, 2 * i_parent + 2,
                           (i_parent_start + i_parent_end) // 2, i_parent_end)


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    # grid = [[int(x) for x in sys.stdin.readline().split()]
    #         for _ in range(N)]  # int grid

    logger.debug('{}'.format([]))

    _max = max(a_list)
    _min = min(a_list)

    st = SegTree(_max - _min + 1)
    retval = 0
    for j in range(N):
        retval += j - st.query(0, a_list[j] + 1 - _min)
        st.update(a_list[j] - _min)

    print(retval)


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
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
1 2 3 4 5 6"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
7 6 5 4 3 2 1"""
        output = """21"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """20
19 11 10 7 8 9 17 18 20 4 3 15 16 1 5 14 6 2 13 12"""
        output = """114"""
        self.assertIO(input, output)
