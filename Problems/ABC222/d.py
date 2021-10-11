import sys

# sys.setrecursionlimit(4100000)

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    b_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    max_b = max(b_list) + 1
    dp = [[0] * max_b for i in range(N)]
    bn = b_list[-1]
    for c in range(a_list[-1], bn + 1):
        dp[N - 1][c] = 1

    for i in range(N - 1)[::-1]:
        dp[i][b_list[i]] = sum(dp[i + 1][b_list[i] : b_list[i + 1] + 1])
        for c in range(a_list[i], b_list[i])[::-1]:
            dp[i][c] = (dp[i][c + 1] + dp[i + 1][c]) % 998244353

    print(sum(dp[0][a_list[0] : b_list[0] + 1]) % 998244353)

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

    def test_入力例_1(self):
        input = """2
1 1
2 3"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
2 2 2
2 2 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
1 2 3 4 5 6 7 8 9 10
1 4 9 16 25 36 49 64 81 100"""
        output = """978222082"""
        self.assertIO(input, output)
