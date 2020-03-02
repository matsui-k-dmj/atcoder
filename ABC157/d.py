import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
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

    def getElementCount(self):  # 要素ごとにそれが属してる集合の要素数を取る
        roots = [self.findRoot(i) for i in range(self.N)]
        counts = Counter(roots)
        return [counts[r] - 1 for r in roots]

    def getRootCount(self):  # ルートごとにそれが属してる集合の要素数を取る
        roots = [self.findRoot(i) for i in range(self.N)]
        counts = Counter(roots)
        return counts


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    N, M, K = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    friend_grid = [[int(x) - 1 for x in sys.stdin.readline().split()]
                   for _ in range(M)]  # int grid

    block_grid = [[int(x) - 1 for x in sys.stdin.readline().split()]
                  for _ in range(K)]  # int grid

    uf = UnionFind(N)
    for a, b in friend_grid:
        uf.unite(a, b)

    count_list = uf.getElementCount()

    for a, b in friend_grid:
        count_list[a] -= 1
        count_list[b] -= 1

    for c, d in block_grid:
        if uf.isSame(c, d):
            count_list[c] -= 1
            count_list[d] -= 1

    print(' '.join([str(c) for c in count_list]))


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
        input = """4 4 1
2 1
1 3
3 2
3 4
4 1"""
        output = """0 1 0 1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 10 0
1 2
1 3
1 4
1 5
3 2
2 4
2 5
4 3
5 3
4 5"""
        output = """0 0 0 0 0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 9 3
10 1
6 7
8 2
2 5
8 4
7 3
10 9
6 4
5 8
2 6
7 5
3 1"""
        output = """1 3 5 4 3 3 3 3 1 0"""
        self.assertIO(input, output)
