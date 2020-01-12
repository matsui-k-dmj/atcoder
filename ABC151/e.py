import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

from functools import lru_cache


def resolve():
    global a_list, N, K

    N, K = [int(x) for x in sys.stdin.readline().split()]
    a_list = [int(x) for x in sys.stdin.readline().split()]

    S = dp(0, -(10**9 + 7), 10**9 + 7, 0)

    print(S % (10**9 + 7))


@lru_cache(maxsize=None)
def dp(i, _max, _min, N_chosen):
    a = a_list[i]
    if i == N - 1:
        if N_chosen == K:
            return (_max - _min) % (10**9 + 7)
        elif N_chosen == K - 1:
            if _max < a:
                _max = a
            if _min > a:
                _min = a
            return (_max - _min) % (10**9 + 7)
        else:
            return 0

    if N_chosen + (N - i) < K:
        return 0

    ex_s = dp(i + 1, _max, _min, N_chosen)

    if N_chosen < K:
        if _max < a:
            _max = a
        if _min > a:
            _min = a
        in_s = dp(i + 1, _max, _min, N_chosen + 1)
    else:
        in_s = 0
    return (ex_s + in_s) % (10**9 + 7)


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
        input = """4 2
1 1 3 4"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 3
10 10 10 -10 -10 -10"""
        output = """360"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 1
1 1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 6
1000000000 1000000000 1000000000 1000000000 1000000000 0 0 0 0 0"""
        output = """999998537"""
        self.assertIO(input, output)
