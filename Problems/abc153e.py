"""
個数制限なしナップサック問題
"""
import sys

# sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    H, N = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int
    a_list, b_list = [], []
    for _ in range(N):
        a, b = sys.stdin.readline().split()
        a_list.append(int(a))
        b_list.append(int(b))

    logger.debug("{}".format([]))

    INF = 10e23
    _H = H + max(a_list)
    dp = [[INF] * _H for i in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for a in range(_H):
            ai = a_list[i]
            bi = b_list[i]
            dp[i + 1][a] = min(dp[i][a], dp[i + 1][a - ai] + bi)

    print(min(dp[N][H:]))


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
        input = """9 3
8 3
4 2
2 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 6
1 1
2 3
3 9
4 27
5 81
6 243"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9999 10
540 7550
691 9680
700 9790
510 7150
415 5818
551 7712
587 8227
619 8671
588 8228
176 2461"""
        output = """139815"""
        self.assertIO(input, output)
