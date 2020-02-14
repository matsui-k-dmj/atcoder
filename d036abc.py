"""dfs, 隣接リスト, ツリーDP
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


@lru_cache(maxsize=None)
def dp(i, color, i_from):
    global neighbor_list, N

    if color:
        # 白
        n_pattern = 1
        for j in neighbor_list[i]:
            if j == i_from:
                continue

            n_pattern *= dp(j, True, i) % (10**9 + 7)

        # 黒
        n_pattern2 = 1
        for j in neighbor_list[i]:
            if j == i_from:
                continue

            n_pattern2 *= dp(j, False, i) % (10**9 + 7)

        return (n_pattern + n_pattern2) % (10**9 + 7)
    else:
        # 白
        n_pattern = 1
        for j in neighbor_list[i]:
            if j == i_from:
                continue

            n_pattern *= dp(j, True, i) % (10**9 + 7)
        return n_pattern % (10**9 + 7)


def resolve():
    global neighbor_list, N

    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    neighbor_list = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = sys.stdin.readline().split()
        a = int(a) - 1
        b = int(b) - 1
        neighbor_list[a].append(b)
        neighbor_list[b].append(a)

    print(dp(0, True, -1) % (10**9 + 7))


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

    def test_入力例1(self):
        input = """5
2 5
1 5
2 4
3 2"""
        output = """14"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """10
7 9
8 1
9 6
10 8
8 6
10 3
5 8
4 8
2 5"""
        output = """192"""
        self.assertIO(input, output)
