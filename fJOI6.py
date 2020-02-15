"""グリッド, グリッドDP
下と右だけ
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

I_DELTA = [
    1,
    0,
]
J_DELTA = [0, 1]


def dfs(i, j):
    global I_MIN, I_MAX, J_MIN, J_MAX, grid, dp
    if dp[i][j] == 0:
        if (i, j) == (I_MAX, J_MAX):
            dp[i][j] = 1
            return 1

        for d in range(2):
            i_next = i + I_DELTA[d]
            j_next = j + J_DELTA[d]
            if I_MIN <= i_next <= I_MAX and J_MIN <= j_next <= J_MAX and (
                    j_next, i_next) not in grid:
                dp[i][j] += dfs(i_next, j_next)

    return dp[i][j]


def resolve():
    global I_MIN, I_MAX, J_MIN, J_MAX, grid, dp
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    a, b = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    n = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    grid = set([
        tuple([int(x) - 1 for x in sys.stdin.readline().split()])
        for _ in range(n)
    ])  # int grid

    I_MIN = 0
    I_MAX = b - 1
    J_MIN = 0
    J_MAX = a - 1

    dp = [[0] * a for i in range(b)]

    logger.debug('{}'.format([]))

    print(dfs(0, 0))


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
        input = """5 4
3
2 2
2 3
4 2"""
        output = """5"""
        self.assertIO(input, output)
