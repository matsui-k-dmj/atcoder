"""
区間スケジューリング
"""
import sys
# sys.setrecursionlimit(4200000)


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# import math

# from collections import defaultdict


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    
    grid = [
        [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    ]  # int grid

    min_list = []
    max_list = []
    for x, y in grid:
        min_list.append(x)
        max_list.append(y)

    i_list = sorted(range(len(min_list)), key=lambda i: max_list[i])

    current_rmax = 0
    count = 0
    for i in i_list:
        if current_rmax < min_list[i]:
            current_rmax = max_list[i] + D - 1
            count += 1

    print(count)

if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest hoge.py
# pypy3 -m unittest hoge.py

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
        input = """3 3
1 2
4 7
5 9"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
1 2
4 7
4 9"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 2
1 100
1 1000000000
101 1000
9982 44353
1000000000 1000000000"""
        output = """3"""
        self.assertIO(input, output)


