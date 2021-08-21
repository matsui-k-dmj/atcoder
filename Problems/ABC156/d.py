"""comb, ncr, フェルマーの小定理

Returns:
    [type]: [description]
"""
import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

# from collections import defaultdict
# d = defaultdict(list)

# from itertools import combinations
# comb = combinations(range(N), 2)

# 累積和
# from itertools import accumulate
# _list = list(accumulate(a_list)

# from functools import lru_cache
# @lru_cache(maxsize=None)
# def setUp(self):
#     dp.cache_clear()


# factのstartを指定しとけば, 計算量O(k)になる
def comb(n, k, mod):
    a = factmod(n, n - k + 1, mod)
    b = factmod(k, 1, mod)

    div = pow(b % mod, mod - 2, mod)  # フェルマーの小定理

    return a * div % mod


def factmod(n, start, mod):
    val = 1
    for i in range(start, n + 1):
        val *= i
        val %= mod
    return val


def resolve():
    global dp

    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    n, a, b = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    # grid = [[int(x) for x in sys.stdin.readline().split()]
    #         for _ in range    (N)]  # int grid

    mod = 10**9 + 7
    print(int((pow(2, n, mod) - 1 - comb(n, a, mod) - comb(n, b, mod)) % mod))


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
        input = """4 1 3"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000000000 141421 173205"""
        output = """34076506"""
        self.assertIO(input, output)
