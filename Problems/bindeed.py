"""
D - Game on a Grid https://atcoder.jp/contests/indeednow-finalb-open/tasks/indeednow_2015_finalb_d
クラスカル法、最小全域木
グリッド
"""
import sys

# # sys.setrecursionlimit(4100000)

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

from functools import reduce
from collections import Counter


class UnionFind:
    def __init__(self, n):
        self.N = n
        self.parent = list(range(n))
        self.rank = [1 for _ in range(n)]

    def findRoot(self, i):
        if self.parent[i] == i:  # 親が自分ならroot
            return i
        else:
            self.parent[i] = self.findRoot(self.parent[i])  # 親をrootに付け替える
            return self.parent[i]

    def unite(self, i, j):
        i_root = self.findRoot(i)
        j_root = self.findRoot(j)
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

    def isSame(self, i, j):
        return self.findRoot(i) == self.findRoot(j)

    def setGroup(self, elements):
        reduce(self.unite, elements)

    def getElementCount(self):  # 要素ごとにそれが属してる集合の要素数を取る
        roots = [self.findRoot(i) for i in range(self.N)]
        counts = Counter(roots)
        return [counts[r] for r in roots]

    def getRootCount(self):  # ルートごとにそれが属してる集合の要素数を取る
        roots = [self.findRoot(i) for i in range(self.N)]
        counts = Counter(roots)
        return counts


def kruskal(N, edge_list):
    """

    Args:
        N (int): [description]
        edge_list (list[int, int, int]): [cost, i, j]
    """
    edge_list = sorted(edge_list)

    union_find = UnionFind(N)

    total_cost = 0
    for edge in edge_list:
        cost, i, j = edge
        if not union_find.isSame(i, j):
            union_find.unite(i, j)
            total_cost += cost

    return total_cost


def ij2n(i, j, H, W):
    return i * W + j


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    H, W = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    sx, sy = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    gx, gy = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int
    grid = [
        [int(x) for x in sys.stdin.readline().split()] for _ in range(H)
    ]  # int grid

    edge_list = []
    delta_list = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    for i in range(H):
        for j in range(W):
            n = i * W + j
            for delta in delta_list:
                new_i = i + delta[0]
                new_j = j + delta[1]
                if 0 <= new_i < H and 0 <= new_j < W:
                    edge_list.append(
                        (-grid[i][j] * grid[new_i][new_j], n, new_i * W + new_j)
                    )

    cost = kruskal(H * W, edge_list)
    print(-cost + sum([sum(row) for row in grid]))

    # logger.debug("{}".format([]))


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

    def test_入力例1(self):
        input = """1 6
2 1
2 1
0 1 2 3 4 0"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 3
1 1
3 3
2 2 2
1 2 1
1 1 1"""
        output = """33"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """10 10
5 2
6 2
31 0 60 19 87 98 35 68 21 41
21 46 85 72 51 13 0 49 19 25
79 82 46 65 30 99 29 44 99 8
39 48 70 99 82 32 25 49 32 54
81 20 57 70 5 40 88 97 56 17
69 54 35 98 7 38 59 91 80 34
28 13 14 28 60 26 82 10 17 100
29 0 27 43 45 88 88 92 21 67
62 33 35 22 26 68 74 95 86 79
68 18 83 72 85 21 72 34 57 77"""
        output = """370423"""
        self.assertIO(input, output)
