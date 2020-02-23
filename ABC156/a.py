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


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    N, R = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    # grid = [[int(x) for x in sys.stdin.readline().split()]
    #         for _ in range(N)]  # int grid

    logger.debug('{}'.format([]))

    if N >= 10:
        print(R)
    else:
        print(R + 100 * (10 - N))


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
        input = """2 2919"""
        output = """3719"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """22 3051"""
        output = """3051"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()