import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    N, K, M = [int(x) for x in sys.stdin.readline().split()]
    a_list = [int(x) for x in sys.stdin.readline().split()]

    an = N * M - sum(a_list)

    if an < 0:
        print(0)
    elif an <= K:
        print(math.ceil(an))
    else:
        print('-1')


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
        input = """5 10 7
8 10 3 6"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 100 60
100 100 100"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 100 60
0 0 0"""
        output = """-1"""
        self.assertIO(input, output)
