"""二分探索
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
# _list = list(accumulate(a_list)


def C(x, ub):
    return x < ub


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    b_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    c_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    # grid = [[int(x) for x in sys.stdin.readline().split()]
    #         for _ in range(N)]  # int grid

    logger.debug('{}'.format([]))

    a_list = sorted(a_list, reverse=True)
    b_list = sorted(b_list, reverse=True)
    c_list = sorted(c_list, reverse=True)

    total_count = 0
    i_b_upper = -1
    i_a_upper = -1

    b_count_list = None
    for c in c_list:
        if b_list[-1] >= c or a_list[-1] >= c:
            break
        i_b_lower = N

        while (i_b_lower - i_b_upper > 1):
            i_b_middle = (i_b_lower + i_b_upper) // 2
            if C(b_list[i_b_middle], c):
                i_b_lower = i_b_middle
            else:
                i_b_upper = i_b_middle

        if b_count_list is None:
            b_count_list = [0 for _ in range(N)]
            for i in range(i_b_lower, N):
                b = b_list[i]
                if a_list[-1] >= b:
                    break
                i_a_lower = N

                while (i_a_lower - i_a_upper > 1):
                    i_a_middle = (i_a_lower + i_a_upper) // 2
                    if C(a_list[i_a_middle], b):
                        i_a_lower = i_a_middle
                    else:
                        i_a_upper = i_a_middle

                b_count_list[i] = N - i_a_lower

                total_count += (N - i_a_lower)

            b_count_list = reversed(b_count_list)
            b_count_list = list(reversed(list(accumulate(b_count_list))))
        else:
            total_count += b_count_list[i_b_lower]

    print(total_count)


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
        input = """2
1 5
2 4
3 6"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 1 1
2 2 2
3 3 3"""
        output = """27"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
3 14 159 2 6 53
58 9 79 323 84 6
2643 383 2 79 50 288"""
        output = """87"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()