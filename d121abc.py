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


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    A, B = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    # grid = [[int(x) for x in sys.stdin.readline().split()]
    #         for _ in range(N)]  # int grid

    logger.debug('{}'.format([]))

    if A == 0 and B == 0:
        print(0)
        return

    if A == 0:
        A = 1

    k = 0
    digit = 1 / 2
    result_bin = []
    while (digit < B):
        k += 1
        digit = int(2 * digit)
        offset = digit - 1
        period = 2 * digit
        # どっちもオフセット以下
        if (A - offset) <= 0 and (B - offset) <= 0:
            result_bin.append(0)
            continue
        # Bだけオフセットより大きい
        if (A - offset) <= 0 and (B - offset) > 0:
            mb = get_m(B, period, offset)
            result_bin.append(under_b(mb, digit))
            continue

        ma = get_m(A, period, offset)
        mb = get_m(B, period, offset)
        # どっちもオフセットより大きい
        # 同じ周期
        if math.ceil((A - offset) / period) == math.ceil(
            (B - offset) / period):

            if ma < digit and mb < digit:
                result_bin.append(mb - ma + 1)
                continue
            elif ma < digit and digit <= mb:
                result_bin.append(digit - ma)
                continue
            else:
                result_bin.append(0)
                continue

        # 違う周期
        if k == 1:
            result_bin.append(
                upper_a(ma, digit) + under_b(mb, digit) +
                math.ceil((B - offset) / period) -
                math.ceil((A - offset) / period) - 1)
            continue
        result_bin.append(upper_a(ma, digit) + under_b(mb, digit))
        continue

    print(int(''.join([str(x % 2) for x in reversed(result_bin)]), 2))


def get_m(x, period, offset):
    return ((x - offset - 1) % period)


def upper_a(m, digit):
    if m >= digit:
        return 0
    else:
        return digit - m


def under_b(m, digit):
    if m >= digit:
        return digit
    else:
        return m + 1


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
        input = """2 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """123 456"""
        output = """435"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """123456789012 123456789012"""
        output = """123456789012"""
        self.assertIO(input, output)
