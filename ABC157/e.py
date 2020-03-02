"""SegTree, 遅い、、、

Returns:
    [type]: [description]
"""
import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


class SegTree:
    """ノードで集合をもつ
    
    Returns:
        [type]: [description]
    """
    def __init__(self, s):

        N = len(s)

        self.default = set([None])

        # 簡単のために要素数を2のべき乗にしておく
        _n = N
        self.n = 1
        while (self.n < _n):
            self.n = self.n * 2

        self.tree = [self.default for _ in range(2 * self.n - 1)]

        for i, c in enumerate(s):
            self.update(i, c)

    def update(self, i, x):
        i = i + self.n - 1
        if x in self.tree[i]:
            return
        else:
            self.tree[i] = set([x])

        # 親を更新
        while (i > 0):
            i = (i - 1) // 2
            l = self.tree[i * 2 + 1]
            r = self.tree[i * 2 + 2]
            self.tree[i] = l | r

    def query(
        self,
        query_start,
        query_end,  # exclusive
        i_parent=0,
        parent_start=0,
        parent_end=None  # exclusive
    ):
        if parent_end is None:
            parent_end = self.n
        if (query_end <= parent_start
                or parent_end <= query_start):  # クエリとレンジが重ならない
            return self.default
        elif (query_start <= parent_start
              and parent_end <= query_end):  # クエリがレンジを完全に含む
            return self.tree[i_parent]
        else:
            return self.query(query_start, query_end, 2 * i_parent + 1,
                           parent_start, (parent_start + parent_end) // 2) | \
                self.query(query_start, query_end, 2 * i_parent + 2,
                           (parent_start + parent_end) // 2, parent_end)


def resolve():
    N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    Q = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ

    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    grid = [[x for x in sys.stdin.readline().split()]
            for _ in range(Q)]  # int grid

    seg = SegTree(S)

    for _type, a, b in grid:
        if _type == '1':
            a = int(a) - 1
            seg.update(a, b)

        else:
            a = int(a) - 1
            b = int(b) - 1
            retset = seg.query(a, b + 1)
            if None in retset:
                print(len(retset) - 1)
            else:
                print(len(retset))


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
        input = """7
abcdbbd
6
2 3 6
1 5 z
2 1 1
1 4 a
1 7 d
2 1 7"""
        output = """3
1
5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
abcdbbd
6
2 3 6
1 5 z
2 1 1
1 4 a
1 7 d
2 1 7"""
        output = """3
1
5"""
        self.assertIO(input, output)
