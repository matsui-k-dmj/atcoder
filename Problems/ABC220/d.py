import sys

# # sys.setrecursionlimit(4100000)

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int
    # grid = [
    #     [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    # ]  # int grid

    # logger.debug("{}".format([]))

    dp = [[0] * 10 for i in range(N)]
    dp[0][a_list[0]] = 1

    MOD = 998244353
    for i in range(1, N):
        for j in range(10):
            a = a_list[i]
            f = (a + j) % 10
            g = (a * j) % 10
            dp[i][f] += dp[i - 1][j] % MOD
            dp[i][g] += dp[i - 1][j] % MOD

    for k in range(10):
        print(dp[N - 1][k] % MOD)


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
2 7 6"""
        output = """1
0
0
0
2
1
0
0
0
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
0 1 2 3 4"""
        output = """6
0
1
1
4
0
1
1
0
2"""
        self.assertIO(input, output)
