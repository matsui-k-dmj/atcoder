import sys
sys.setrecursionlimit(4100000)

import logging

# logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

import math


def resolve():
    X, Y = [int(x) for x in sys.stdin.readline().split()]

    logger.debug('{} {}'.format(X, Y))

    count = 1
    while (True):
        X = X * 2
        if X > Y:
            break
        else:
            count += 1

    print(count)


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
        input = """3 20"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """25 100"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """314159265 358979323846264338"""
        output = """31"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """3 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_6(self):
        input = """999999999999999999 1000000000000000000"""
        output = """1"""
        self.assertIO(input, output)