import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import math


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, L, R = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # logger.debug("{}".format([]))

    n_bin = bin(N)[2:]
    max_k = len(n_bin)
    count = 0
    for i, x in enumerate(n_bin):
        if x == "0":
            continue
        k = max_k - i
        x_min = 2 ** (k - 1)
        x_max = 2 ** k - 1
        l = max(x_min, L)
        r = min(x_max, R)
        count += max(r - l + 1, 0)

    print(count)


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
        input = """2 1 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 2 19"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000000000000 1 1000000000000000000"""
        output = """847078495393153025"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 1 1"""
        output = """1"""
        self.assertIO(input, output)
