"""
D - Equals https://atcoder.jp/contests/arc097/tasks/arc097_b
UnionFind
何回でもスワップできたら、スワップできるペアでつながってる集合は任意の順番に入れ替えれる
p_i と iが同じグループに入ってたらいいってこと。
"""
import sys

# sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

from functools import reduce
from collections import Counter


class UnionFind:
    def __init__(self, n):
        self.N = n
        self.parent = list(range(n))
        self.rank = [1 for _ in range(n)]

    def find_root(self, i):
        if self.parent[i] == i:  # 親が自分ならroot
            return i
        else:
            self.parent[i] = self.find_root(self.parent[i])  # 親をrootに付け替える
            return self.parent[i]

    def unite(self, i, j):
        i_root = self.find_root(i)
        j_root = self.find_root(j)
        if i_root == j_root:
            return

        if self.rank[i_root] > self.rank[j_root]:  # ランクが高い方を親にする。
            self.parent[j_root] = i_root
        elif self.rank[i_root] == self.rank[j_root]:
            self.parent[j_root] = i_root
            self.rank[i_root] += 1
        else:
            self.parent[i_root] = j_root

        return i

    def is_same(self, i, j):
        return self.find_root(i) == self.find_root(j)

    def set_group(self, elements):
        reduce(self.unite, elements)

    def get_element_count(self):  # 要素ごとにそれが属してる集合の要素数を取る
        roots = [self.find_root(i) for i in range(self.N)]
        counts = Counter(roots)
        return [counts[r] for r in roots]

    def get_root_count(self):  # ルートごとにそれが属してる集合の要素数を取る
        roots = [self.find_root(i) for i in range(self.N)]
        counts = Counter(roots)
        return counts


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, M = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    p_list = [int(x) - 1 for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int
    grid = [
        [int(x) - 1 for x in sys.stdin.readline().split()] for _ in range(M)
    ]  # int grid

    logger.debug("{}".format([]))

    uf = UnionFind(N)
    for x, y in grid:
        uf.unite(x, y)

    s = 0
    for i, p in enumerate(p_list):
        s += uf.is_same(i, p)

    print(s)


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
        input = """5 2
5 3 1 4 2
1 3
5 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
3 2 1
1 2
2 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 8
5 3 6 8 7 10 9 1 2 4
3 1
4 1
5 9
2 5
6 5
3 5
8 9
7 9"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5 1
1 2 3 4 5
1 5"""
        output = """5"""
        self.assertIO(input, output)
