"""
C - One-stroke Path https://atcoder.jp/contests/abc054/tasks/abc054_c

一筆書き
n = 8なので、n!でやってもよい。
bitDPすると2^n n^2
"""
import sys

# # sys.setrecursionlimit(4100000)

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

import math


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, M = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int
    edge_list = [[] for _ in range(N)]
    for _ in range(M):
        a, b = [int(x) - 1 for x in sys.stdin.readline().split()]
        edge_list[a].append(b)
        edge_list[b].append(a)

    # logger.debug("{}".format([]))

    dp = [[0] * N for i in range(1 << N)]

    dp[1][0] = 1  # dp[{0}][0]

    for s in range(1 << N):
        for v in range(N):
            if not (s >> v) & 1:
                continue

            tmp = 0
            for e in edge_list[v]:
                if (s >> e) & 1:
                    tmp += dp[s & ~(1 << v)][e]

            dp[s][v] += tmp

    tmp = dp[(1 << N) - 1]
    print(sum(tmp[i] for i in range(N)))


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
        input = """7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7"""
        output = """1"""
        self.assertIO(input, output)
