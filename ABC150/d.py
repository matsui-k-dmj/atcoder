"""
最小公倍数
"""

import sys
sys.setrecursionlimit(4100000)

import math
import fractions
from functools import reduce

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


def resolve():
    N, M = [int(x) for x in sys.stdin.readline().split()]
    a_list = [int(x) for x in sys.stdin.readline().split()]

    L = lcm_list(a_list)
    if any([(L // a) % 2 == 0 for a in a_list]):
        print(0)
        return
    else:
        print(M // L + 1)


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
        input = """2 50
6 10"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 100
14 22 40"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 1000000000
6 6 2 6 2"""
        output = """166666667"""
        self.assertIO(input, output)
