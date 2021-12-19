"""
グリッドを集合に分ける
"""

import sys
# sys.setrecursionlimit(4200000)


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# import math



def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    H, W, K = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    x1, y1, x2, y2 = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    a, b, c, d = 0, 0, 0, 0
    if x1 == x2 and y1 == y2:
        d = 1
    elif x1 == x2:
        c = 1
    elif y1 == y2:
        b = 1
    else:
        a = 1

    MOD = 998244353

    for k in range(K):
        new_a = (H - 2 + W - 2) * a + (H - 1) * c + (W - 1) * b
        new_b = a + (H - 1) * d + (H - 2) * b
        new_c = a + (W - 1) * d + (W - 2) * c
        new_d = b + c
        a, b, c, d = new_a % MOD, new_b % MOD, new_c % MOD, new_d % MOD

    print(d)


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
        input = """2 2 2
1 2 2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000000000 1000000000 1000000
1000000000 1000000000 1000000000 1000000000"""
        output = """24922282"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 3 3
1 3 3 3"""
        output = """9"""
        self.assertIO(input, output)


