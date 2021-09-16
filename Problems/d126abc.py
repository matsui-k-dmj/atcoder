"""
D - Even Relation https://atcoder.jp/contests/abc126/tasks/abc126_d
DFS
2部グラフ
"""
import sys

sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int
    # grid = [
    #     [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    # ]  # int grid
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = [int(x) for x in sys.stdin.readline().split()]
        graph[u - 1].append((v - 1, w))
        graph[v - 1].append((u - 1, w))

    color_list = [-1] * N

    def dfs(i_node, col):
        color_list[i_node] = col
        for v_node, w in graph[i_node]:
            if w % 2 == 0:
                next_col = col
            else:
                next_col = 1 - col

            if color_list[v_node] == -1:
                dfs(v_node, next_col)

    dfs(0, 0)

    for c in color_list:
        print(c)


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
        input = """3
1 2 2
2 3 1"""
        output = """0
0
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
2 5 2
2 3 10
1 3 8
3 4 2"""
        output = """0
0
0
0
0"""
        self.assertIO(input, output)
