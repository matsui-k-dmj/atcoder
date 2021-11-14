import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import math


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ

    count = 0
    for a in range(1, N + 1):
        for b in range(a, N + 1):
            for c in range(b, N + 1):
                if a * b * c <= N:
                    count += 1
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
        input = """4"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100"""
        output = """323"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000000000"""
        output = """5745290566750"""
        self.assertIO(input, output)
