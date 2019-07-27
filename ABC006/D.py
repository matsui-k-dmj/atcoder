"""
LIS
"""

import sys
sys.setrecursionlimit(4100000)

import logging

# logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

# @profile
def resolve():
    N = int(sys.stdin.readline().split()[0])
    c_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]

    logger.debug('{} {}'.format(N, c_list))

    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if c_list[j] <= c_list[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    logger.debug(dp)
    print(N - max(dp))

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
        input = """6
1
3
5
2
4
6"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5
5
4
3
2
1"""
        output = """4"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """7
1
2
3
4
5
6
7"""
        output = """0"""
        self.assertIO(input, output)