"""グリッド, グリッドDP
Python3
lru_cache あり
1.92sec
lru_cache なし
8.8sec
自分でcache
1.8sec

pypy3
lru_cache あり
1.4sec
lru_cache なし
1.2sec

===========
自分でcache
0.6sec
===========
"""

import sys
sys.setrecursionlimit(10**9)

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

I_DELTA = [1, 0, -1, 0]
J_DELTA = [0, -1, 0, 1]

MOD = (10**9 + 7)


# @lru_cache(maxsize=None)
def dfs(i, j):
    global I_MIN, I_MAX, J_MIN, J_MAX, grid, dp

    if dp[i][j] == 0:
        dp[i][j] = 1  # とどまるので１パターン
        for d in range(4):
            i_next = i + I_DELTA[d]
            j_next = j + J_DELTA[d]
            if I_MIN <= i_next <= I_MAX and J_MIN <= j_next <= J_MAX and grid[
                    i_next][j_next] > grid[i][j]:
                dp[i][j] += dfs(i_next, j_next) % MOD

    return dp[i][j]


def resolve():
    global I_MIN, I_MAX, J_MIN, J_MAX, grid, dp

    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    H, W = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    grid = [[int(x) for x in sys.stdin.readline().split()]
            for _ in range(H)]  # int grid

    logger.debug('{}'.format([]))

    I_MIN = 0
    I_MAX = H - 1
    J_MIN = 0
    J_MAX = W - 1

    dp = [[0] * W for i in range(H)]

    for i in range(H):
        for j in range(W):
            dfs(i, j)

    print(sum([sum(row) % MOD for row in dp]) % MOD)


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
        dfs.cache_clear()

    def test_入力例_1(self):
        input = """2 3
1 4 5
2 4 9"""
        output = """18"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 6
1 3 4 6 7 5
1 2 4 8 8 7
2 7 9 2 7 2
9 4 2 7 6 5
2 8 4 6 7 6
3 7 9 1 2 7"""
        output = """170"""
        self.assertIO(input, output)
