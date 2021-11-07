"""
無向グラフ
連結グラフ
連結成分数え上げ
"""
import sys

sys.setrecursionlimit(1000000000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, M = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    edge_list = [[] for _ in range(N)]
    for i in range(M):
        a, b = [int(x) - 1 for x in sys.stdin.readline().split()]
        edge_list[a].append((b, i))
        edge_list[b].append((a, i))

    visited_set = set()
    visited_edge = set()

    def dfs(i, parent_i):
        visited_set.add(i)

        for next_i, edge_i in edge_list[i]:
            visited_edge.add(edge_i)
            if next_i != parent_i and next_i not in visited_set:
                dfs(next_i, i)

        return

    count = 0
    for i in range(N):
        if i not in visited_set:
            dfs(i, -1)
            if len(visited_set) == len(visited_edge):
                count += 1
            else:
                print(0)
                return
    print(pow(2, count, 998244353))


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
        input = """3 3
1 2
1 3
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 1
1 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 7
1 2
2 3
3 4
4 2
5 6
6 7
7 5"""
        output = """4"""
        self.assertIO(input, output)
