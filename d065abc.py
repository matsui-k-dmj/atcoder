"""最小全域木, クラスカル法, kruskal
"""

import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
from collections import defaultdict
# d = defaultdict(list)

from itertools import combinations
# comb = combinations(range(N), 2)

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


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    grid = [[int(x) for x in sys.stdin.readline().split()] + [i]
            for i in range(N)]  # int grid

    logger.debug('{}'.format([]))

    edge_list = []
    # x でソート
    grid = sorted(grid, key=lambda xy: xy[0])
    for i in range(N - 1):
        xi, yi, vi = grid[i]
        xj, yj, vj = grid[i + 1]
        edge_list.append((min(abs(xi - xj), abs(yi - yj)), vi, vj))

    # y でソート
    grid = sorted(grid, key=lambda xy: xy[1])

    for i in range(N - 1):
        xi, yi, vi = grid[i]
        xj, yj, vj = grid[i + 1]
        edge_list.append((min(abs(xi - xj), abs(yi - yj)), vi, vj))

    print(kruskal(N, edge_list))


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
        input = """3
1 5
3 9
7 8"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
8 3
4 9
12 19
18 1
13 5
7 6"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
0 0
0 0"""
        output = """0"""
        self.assertIO(input, output)