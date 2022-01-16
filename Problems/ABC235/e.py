
import sys
# sys.setrecursionlimit(4200000)


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

def kruskal(N, edge_list, Q):
    """

    Args:
        N (int): [description]
        edge_list (list[int, int, int]): [cost, i, j]
    """
    edge_list = sorted(edge_list, key=lambda x: x[0])

    union_find = UnionFind(N)

    return_list = [""] * Q
    for edge in edge_list:
        cost, i, j, ok, i_query = edge
        if ok:
            if not union_find.isSame(i, j):
                union_find.unite(i, j)
        else:
            if union_find.isSame(i, j):
                return_list[i_query] = 'No'
            else:
                return_list[i_query] = 'Yes'


    return return_list

def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, M, Q = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    edge_list = []
    for _ in range(M):
        a, b, c = [int(x) for x in sys.stdin.readline().split()]
        edge_list.append((c, a-1, b-1, True, -1))
    for i in range(Q):
        a, b, c = [int(x) for x in sys.stdin.readline().split()]
        edge_list.append((c, a-1, b-1, False, i))

    # logger.debug("{}".format([]))

    _list = kruskal(N, edge_list, Q)

    for ans in _list:
        print(ans)




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
        input = """5 6 3
1 2 2
2 3 3
1 3 6
2 4 5
4 5 9
3 5 8
1 3 1
3 4 7
3 5 7"""
        output = """Yes
No
Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3 2
1 2 100
1 2 1000000000
1 1 1
1 2 2
1 1 5"""
        output = """Yes
No"""
        self.assertIO(input, output)


