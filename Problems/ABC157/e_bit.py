"""SegTree, bitで集合を管理する

Returns:
    [type]: [description]
"""
import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

from operator import or_


class SegTree:
    """SegTree
    """
    def __init__(self, N, segfunc, ide, initial_list=None):

        self.ide = ide
        self.segfunc = segfunc

        # 簡単のために要素数を2のべき乗にしておく
        _n = N
        self.n = 1
        while (self.n < _n):
            self.n = self.n * 2

        self.tree = [self.ide for _ in range(2 * self.n - 1)]

        if initial_list is not None:
            for i, v in enumerate(initial_list):
                self.update(i, v)

    def update(self, i, x):
        i = i + self.n - 1
        self.tree[i] = x

        # 親を更新
        while (i > 0):
            i = (i - 1) // 2
            l = self.tree[i * 2 + 1]
            r = self.tree[i * 2 + 2]
            self.tree[i] = self.segfunc(l, r)

    def query(self, l, r):
        """https://proc-cpuinfo.fixstars.com/2017/07/optimize-segment-tree/
        
        Args:
            l (int): 左 inclusive
            r (int): 右 exclusive
        """
        l += (self.n - 1)
        r += (self.n - 1)
        res = self.ide
        while l < r:
            if l & 1 == 0:  # 奇数のとき。l += (self.n - 1)してるから
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1 == 0:
                res = self.segfunc(res, self.tree[r - 1])
                r -= 1

            l = l // 2
            r = r // 2

        return res


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

    seg = SegTree(N, or_, 0, [1 << ord(c) - 97 for c in S])

    for _type, a, b in grid:
        if _type == '1':
            a = int(a) - 1
            bit = 1 << (ord(b) - 97)
            seg.update(a, bit)

        else:
            a = int(a) - 1
            b = int(b) - 1
            ret = seg.query(a, b + 1)
            print(bin(ret)[2:].count('1'))


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
