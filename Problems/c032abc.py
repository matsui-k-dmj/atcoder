"""しゃくとり法
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
from itertools import accumulate
# _list = list(accumulate(a_list)  # s[i] = s0 + s1 + ... + si-1 + si, なので sum(origin[i_start: i_end]) == s[i_end - 1] - s[i_start - 1]


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    N, K = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    s_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    # grid = [[int(x) for x in sys.stdin.readline().split()]
    #         for _ in range(N)]  # int grid

    logger.debug('{}'.format([]))

    if any([s == 0 for s in s_list]):
        print(len(s_list))
        return

    max_len = 0
    i_start = 0
    i_end = 0
    prod = 1
    while (i_end <= N - 1 and i_start <= N - 1):
        while (i_end <= N - 1):
            i_end += 1  # 加えて
            prod *= s_list[i_end - 1]  # 進める
            if (prod <= K):
                max_len = max(max_len, i_end - i_start)
            else:
                break

        prod /= s_list[i_start]  # 引いて
        i_start += 1  # 進める
    print(max_len)


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

    def test_入力例1(self):
        input = """7 6
4
3
1
1
2
10
2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6 10
10
10
10
10
0
10"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """6 9
10
10
10
10
10
10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """4 0
1
2
3
4"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """7 1
1
1
1
1
1
1
1"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例6(self):
        input = """7 2
1
1
1
1
1
1
2"""
        output = """7"""
        self.assertIO(input, output)