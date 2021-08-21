"""max min 探索

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
from functools import lru_cache


@lru_cache(maxsize=None)
def dp(i, j, is_myturn):
    global A, B, a_list, b_list
    if is_myturn:
        if i < A and j < B:
            return max(
                dp(i + 1, j, False) + a_list[i],
                dp(i, j + 1, False) + b_list[j])
        elif i < A:
            return dp(i + 1, j, False) + a_list[i]
        elif j < B:
            return dp(i, j + 1, False) + b_list[j]
        else:
            return 0
    else:
        if i < A and j < B:
            return min(dp(i + 1, j, True), dp(i, j + 1, True))
        elif i < A:
            return dp(i + 1, j, True)
        elif j < B:
            return dp(i, j + 1, True)
        else:
            return 0


def resolve():
    global A, B, a_list, b_list
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    A, B = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    b_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    # grid = [[int(x) for x in sys.stdin.readline().split()]
    #         for _ in range(N)]  # int grid

    logger.debug('{}'.format([]))

    print(dp(0, 0, True))


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

    def setUp(self):
        dp.cache_clear()

    def test_Sample_Input_1(self):
        input = """1 2
1
2 10"""
        output = """11"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 5
2 4 5 4 2
2 8 3 4 5"""
        output = """21"""
        self.assertIO(input, output)
