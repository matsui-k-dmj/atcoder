import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

from functools import reduce

from collections import Counter


class UnionFind:
    def __init__(self, n):
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


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    N, K, L = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    grid = [
        tuple([int(x) - 1 for x in sys.stdin.readline().split()])
        for _ in range(K + L)
    ]  # int grid

    logger.debug('{}'.format([]))

    p_uf = UnionFind(N)
    r_uf = UnionFind(N)
    both_uf = UnionFindCounter(N)

    for k in range(K):
        p, q = grid[k]
        p_uf.unite(p, q)

    for l in range(K, K + L):
        r, s = grid[l]
        r_uf.unite(r, s)

    # for (p, q) in combinations(range(N), 2):
    #     if p_uf.isSame(p, q) and r_uf.isSame(p, q):
    #         both_uf.unite(p, q)

    pairs = [(p_uf.findRoot(i), r_uf.findRoot(i)) for i in range(N)]

    counts = Counter(pairs)

    print(' '.join([str(counts[pairs[i]]) for i in range(N)]))


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
        input = """4 3 1
1 2
2 3
3 4
2 3"""
        output = """1 2 2 1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 2 2
1 2
2 3
1 4
2 3"""
        output = """1 2 2 1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 4 4
1 2
2 3
2 5
6 7
3 5
4 5
3 4
6 7"""
        output = """1 1 2 1 2 2 2"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2 1 1
1 2
1 2"""
        output = """2 2"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """4 3 3
1 2
1 4
1 3
1 4
4 3
2 3"""
        output = """4 4 4 4"""
        self.assertIO(input, output)

    def test_入力例_6(self):
        input = """5 3 4
1 2
2 3
3 4
1 5
5 4
4 3
3 2"""
        output = """4 4 4 4 1"""
        self.assertIO(input, output)